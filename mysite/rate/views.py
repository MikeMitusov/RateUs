from django.shortcuts import render
from django.views.generic import ListView
from .models import Author, Link, Review


class AuthorListView(ListView):
    model = Author
    queryset = Author.objects.filter(active=True)
    context_object_name = "author"
    template_name = "rate/author/list.html"
    paginate_by = 3
