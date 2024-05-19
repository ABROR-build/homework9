from . import models
from django.views.generic import ListView, DetailView


class Dashboard(ListView):
    model = models.Blogs
    template_name = 'dashboard.html'
    context_object_name = 'blogs'


class BlogDetail(DetailView):
    model = models.Blogs
    template_name = 'detailed.html'
    context_object_name = 'blog'
    print('--------------------------Detail is working---------------------')
