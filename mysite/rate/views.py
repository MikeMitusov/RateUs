from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Author, Link, Review


class AuthorListView(ListView):
    model = Author
    queryset = Author.objects.filter(active=True)
    context_object_name = "authors"
    template_name = "rate/author/list.html"
    paginate_by = 3


def author_detail(request, author_id):
    author = get_object_or_404(Author, active=True, id=author_id)

    return render(request, "rate/author/detail.html", {"author": author})
