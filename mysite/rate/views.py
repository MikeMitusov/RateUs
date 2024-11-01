from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Author, Link, Review
from .forms import WriteReviewForm, WriteEmailForm


class AuthorListView(ListView):
    model = Author
    queryset = Author.objects.filter(active=True)
    context_object_name = "authors"
    template_name = "rate/author/list.html"
    paginate_by = 3


def author_detail(request, author_id):
    author = get_object_or_404(Author, active=True, id=author_id)
    reviews = Review.objects.filter(active=True, author=author)
    reviews = Paginator(reviews, 5)

    try:
        num = request.GET.get("page", 1)
        if num == "-1":
            num = reviews.num_pages
        page_obj = reviews.page(num)
    except PageNotAnInteger:
        page_obj = reviews.page(1)
    except EmptyPage:
        page_obj = reviews.page(1)

    return render(
        request, "rate/author/detail.html", {"author": author, "reviews": page_obj}
    )


def review_detail(request, author_id, review_id):
    author = get_object_or_404(Author, id=author_id, active=True)
    review = get_object_or_404(Review, active=True, author=author, id=review_id)

    return render(request, "rate/review/detail.html", {"review": review})


def review_write(request, author_id):
    author = get_object_or_404(Author, id=author_id)

    if request.method == "POST":
        form = WriteReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.author = author
            review.save()
            return redirect(
                reverse("rate:author_detail", args=(author_id,)) + "?page=-1"
            )
    else:
        form = WriteReviewForm()
        review = None

    return render(
        request,
        "rate/review/write.html",
        {"form": form, "author": author},
    )


def author_write(request, author_id):
    author = get_object_or_404(Author, id=author_id, active=True)

    if request.method == "POST":
        form = WriteEmailForm(request.POST)

        if form.is_valid():
            # send email
            return redirect(reverse("rate:author_detail", args=(author_id,)))
    else:
        form = WriteEmailForm()

    return render(
        request, "rate/author/form_write.html", {"author": author, "form": form}
    )
