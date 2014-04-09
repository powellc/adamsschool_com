from django.contrib import messages
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.dates import YearArchiveView, MonthArchiveView

import mailchimp
from .forms import NewsletterSignupForm
from .models import Edition


class EditionYearArchiveView(YearArchiveView):
    queryset = Edition.published_objects.all()
    date_field = 'publish_on'
    make_object_list = True


class EditionMonthArchiveView(MonthArchiveView):
    queryset = Edition.published_objects.all()
    date_field = 'publish_on'
    make_object_list = True


class EditionDetailView(DetailView):
    model = Edition
    template_name = 'newsletters/newsletter.html'
    slug_field = 'id'


class EditionListView(ListView):
    queryset = Edition.published_objects.all()
    template_name = 'newsletters/newsletter-archive-list.html'


class NewsletterView(TemplateView):
    template_name = 'newsletters/newsletter.html'

    def get_context_data(self, **kwargs):
        context = super(NewsletterView, self).get_context_data(**kwargs)
        try:
            context['object'] = Edition.published_objects.latest()
        except:
            context['object'] = None
        return context


letter = mailchimp.utils.get_connection().get_list_by_id(getattr(
    settings, 'MAILCHIMP_NEWSLETTER_LIST_ID', None))

parents = mailchimp.utils.get_connection().get_list_by_id(getattr(
    settings, 'MAILCHIMP_PARENTS_LIST_ID', None))

saved_lists = {'parents': parents,
               'letter': letter}


def update_subscription(list1, email_address, fname=None, lname=None,
                        subscribe=False, unsubscribe=False):
    if email_address:
        try:
            subscriber = list1.get_member(email_address)
        except:
            subscriber = None
        if not subscriber and subscribe:
            list1.subscribe(email_address,{'EMAIL': email_address, 'FNAME': fname, 'LNAME':lname})
            return (True, 'has been successfully subscribed to')
        elif subscriber and subscriber.info['status'] == 'unsubscribed' and subscribe:
            list1.subscribe(email_address,{'EMAIL': email_address, 'FNAME': fname, 'LNAME':lname})
            return (True, 'has been successfully subscribed to')
        elif not subscriber and not subscribe:
            return (False, 'is not subscribed to')
        elif subscriber.info['status'] == 'subscribed' and unsubscribe:
            list1.unsubscribe(email_address,{'EMAIL': email_address,})
            return (True, 'has been successfully unsubscribed from')
        elif subscriber and not unsubscribe:
            return (False, 'is already subscribed to')
        elif subscriber and subscriber.info['status'] == 'unsubscribed' and unsubscribe:
            return (False, 'is not subscribed to')
    else:
        return (False, 'no email address')

def subscribe(request):
    form = NewsletterSignupForm(request.POST or None)

    if form.is_valid():
        user_subscribed = False
        update_string = [] # This just keeps track of what were doing for messages
        email_address = form.cleaned_data['email_address']
        if request.POST.get('lists', False):
            for li in request.POST['lists'].split(','):
                update_string.append(li)
                success, response = update_subscription(saved_lists[li], email_address, subscribe=True)
                if success:
                    user_subscribed = False
            messages.success(request, '<b>%s</b> %s our %s newsletters.'
                    % (email_address, response, ' and '.join(update_string)))
            return HttpResponseRedirect(reverse('newsletter-confirmation'))
        else:
            pass
    return render_to_response('newsletters/subscribe-form.html', {
        'form': form
    }, context_instance=RequestContext(request))

def confirmation(request):
    return render_to_response('newsletters/thank_you.html', {
    }, context_instance=RequestContext(request))
