from django.shortcuts import render
from django.views.generic import ListView

from .models import Article

class BlogListView(ListView):
    """
    View for displaying a list of blog articles.

    This view retrieves a queryset of articles with related data pre-fetched and passes it to the template
    for rendering.

    Attributes:
        queryset (QuerySet): The queryset of articles with related data pre-fetched.
        template_name (str): The template to render for the blog list view.
        context_object_name (str): The variable name to use in the template for the queryset.
    """
    queryset = (
        Article.objects
        .select_related('author')
        .select_related('category')
        .prefetch_related('tags')
    )

    template_name = 'blogapp/blog-list.html'
    context_object_name = 'articles'
