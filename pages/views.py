from django.http import HttpResponse
from django.template import loader
from pages.models import Page
import html

def index(request):
    template = loader.get_template('pages/index.html')
    context = {
        'pages': Page.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def view(request, page_url):
    template = loader.get_template('pages/view.html')
    context = {
        'html': html.unescape(Page.objects.filter(url=page_url).get().html),
    }
    return HttpResponse(template.render(context, request))