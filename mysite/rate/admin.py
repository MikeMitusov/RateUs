from django.contrib import admin
from .models import Author, Review, Link


class LinkInline(admin.TabularInline):
    extra = 1
    max_num = 5
    model = Link


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "bio", "active"]
    search_fields = ["name", "email", "bio"]
    list_filter = ["created", "updated", "active", "allow_mail"]
    inlines = [LinkInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["rating", "author", "name", "email", "created", "active"]
    search_fields = ["author", "name", "email", "body"]
    raw_id_fields = ["author"]
    date_hierarchy = "created"
    list_filter = ["rating", "created", "active"]
