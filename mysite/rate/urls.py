from django.urls import path
from . import views


app_name = "rate"

urlpatterns = [
    path("", views.AuthorListView.as_view(), name="author_list"),
    path("<int:author_id>", views.author_detail, name="author_detail"),
    path("<int:author_id>/<int:review_id>", views.review_detail, name="review_detail"),
    path("<int:author_id>/review", views.review_write, name="review_write"),
]
