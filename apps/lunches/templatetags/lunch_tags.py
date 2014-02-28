from django import template
from classytags.core import Tag, Options
from classytags.arguments import Argument
from lunches.models import LunchMenu

register = template.Library()



class CurrentMenu(Tag):
    ''' Get the latest menu and wedge it in a variable '''
    name = 'current_menu'
    options = Options(
        'as',
        Argument('varname', required=True, resolve=False)
    )

    def render_tag(self, context, varname):
        menu = LunchMenu.objects.latest()
        context[varname] = menu
        return ''
register.tag(CurrentMenu)
