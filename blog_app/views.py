from django.shortcuts import render
from django.views.generic import (ListView, DetailView, 
        TemplateView)
from blog_app.models import BlogPost
# Create your views here.

class MainPageView(ListView):
    
    queryset = BlogPost.objects.all()
    context_object_name = "posts"
    template_name = "blog_app/index.html"

class PostDetailView(DetailView):

    model = BlogPost
    context_object_name = "post"


class About(TemplateView):

    template_name = "blog_app/about.html"

