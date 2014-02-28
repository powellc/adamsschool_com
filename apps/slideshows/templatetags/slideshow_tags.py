from django import template
from classytags.core import Tag, Options
from classytags.arguments import Argument
from slideshows.models import Slideshow

register = template.Library()


#@register.inclusion_tag('slideshows/slideshow.html')
#def slideshow(slug):
#    try:
#        slideshow = Slideshow.objects.get(slug=slug)
#    except Slideshow.DoesNotExist:
#        return {}
#    return {'slideshow': slideshow}


class SlideshowTag(Tag):
    name = 'active_slideshow'
    options = Options(
        'as',
        Argument('varname', required=True, resolve=False)
    )

    def render_tag(self, context, varname):
        try:
            slideshow = Slideshow.objects.get(active=True)
        except:
            slideshow = []
        context[varname] = slideshow
        return ''
register.tag(SlideshowTag)
