from django.urls import path
from . import views


app_name = "rate"

urlpatters = [
    path("<int:author_id>", views.AuthorListView.as_view(), name="author_list")
]
