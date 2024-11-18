from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "post_list.html"
    template_name = "blog/index.html"
    paginate_by = 6

def index(request): 
    return render(request, 'blog/index.html')