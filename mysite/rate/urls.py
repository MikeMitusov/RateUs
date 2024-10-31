from django.urls import path
from . import views


app_name = "rate"

urlpatterns = [
    path("", views.AuthorListView.as_view(), name="author_list"),
    path("<int:author_id>", views.author_detail, name="author_detail"),
]
