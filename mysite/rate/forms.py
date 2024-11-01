from django import forms
from .models import Review


class WriteReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "name", "email", "body"]


class WriteEmailForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    body = forms.CharField(max_length=10_000, widget=forms.Textarea)
