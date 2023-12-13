from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy

from .models import Blog
# Create your views here.
def index(request):
    blog_home = Blog.objects.order_by('-create_date')
    context = {'blog_home': blog_home}
    return render(request, 'blog/blog_home.html', context)

def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    context = {'blog': blog}
    return render(request, 'blog/blog_detail.html', context)

class create(generic.CreateView):
    model = Blog
    fields = ['title', 'content', 'create_date', 'categories']
    success_url = reverse_lazy('blog:home')
    template_name_suffix = '_create'

# class delete(generic.DeleteView):
#     model = Blog
#     fields = ['title', 'content', 'create_date', 'categories']
#     success_url = reverse_lazy('blog:home')
#     template_name_suffix = '_delete.html'