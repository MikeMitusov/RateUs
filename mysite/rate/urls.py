from django.urls import path
from . import views


app_name = "rate"

urlpatterns = [
    path("<int:author_id>", views.AuthorListView.as_view(), name="author_list")
]
