from django.shortcuts import render
from django.views.generic import ListView

from .models import Article

class BlogListView(ListView):
    queryset = (
        Article.objects
        .select_related('author')
        .select_related('category')
        .prefetch_related('tags')
    )

    template_name = 'blogapp/blog-list.html'
    context_object_name = 'articles'