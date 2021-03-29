from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template_name = 'index.html'
    template = loader.get_template(template_name)
    context = {
        'title': 'Home',
        'description': 'Welcome to cooperparlee.com, my personal-website portfolio!',
    }
    return HttpResponse(template.render(context, request))