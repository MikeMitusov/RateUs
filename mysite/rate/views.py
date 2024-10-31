from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Author, Link, Review
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class AuthorListView(ListView):
    model = Author
    queryset = Author.objects.filter(active=True)
    context_object_name = "authors"
    template_name = "rate/author/list.html"
    paginate_by = 3


def author_detail(request, author_id):
    author = get_object_or_404(Author, active=True, id=author_id)
    reviews = Review.objects.filter(active=True, author=author)
    reviews = Paginator(reviews, 3)

    try:
        page_obj = reviews.page(request.GET.get("page", 1))
    except PageNotAnInteger:
        page_obj = reviews.page(1)
    except EmptyPage:
        page_obj = reviews.page(1)

    return render(
        request, "rate/author/detail.html", {"author": author, "reviews": page_obj}
    )
