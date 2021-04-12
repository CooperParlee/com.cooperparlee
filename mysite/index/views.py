from django.http import HttpResponse
from django.template import loader
from blog.models import Post

import array

# Create your views here.
def index(request):
    template_name = 'index.html'
    template = loader.get_template(template_name)
    posts = {}
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]

    print(queryset)

    context = {
        'title': 'Home',
        'description': 'Welcome to cooperparlee.com, my personal-website portfolio!',
        'posts': queryset,
    }
    return HttpResponse(template.render(context, request))