from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

from .services import get_filename_by, validate_avatar


class Author(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    avatar = models.ImageField(
        upload_to="uploads/%Y/%m/%d/", validators=[validate_avatar]
    )
    bio = models.TextField()
    allow_mail = models.BooleanField(
        "Allow clients to send emails to author", default=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["created"]
        indexes = [models.Index(fields=["created"])]

    def get_absolute_url(self):
        return reverse("rate:author_detail", args=[self.id])

    def get_rating(self):
        return round(
            self.reviews.all().aggregate(models.Avg("rating"))["rating__avg"], 1
        )


class Link(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="links")
    title = models.CharField(max_length=20)
    url = models.URLField()
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["title"]
        indexes = [models.Index(fields=["title"])]

    def get_icon_url(self):
        url = self.url
        if not url.find("x.com"):
            url = url.translate(["x", ""])
        return get_filename_by(url)


class Review(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    name = models.CharField(max_length=40)
    email = models.EmailField()
    body = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]
        indexes = [models.Index(fields=["created"])]
