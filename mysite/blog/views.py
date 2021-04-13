from django.views import generic
from .models import Post

# Create your views here.
class PostList (generic.ListView):
    queryset = Post.objects.filter(status=1, hidden=False).order_by('-created_on')
    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Articles'
        context['description'] = 'Recently posted projects on cooperparlee.com'
        return context

    
    template_name = 'post_list.html'

class PostDetail(generic.DetailView):
    model = Post
    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(kwargs)
        context['title'] = kwargs.get('object')
        context['description'] = kwargs.get('object').info()
        return context
    

    template_name = 'post_detail.html'