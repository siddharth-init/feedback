from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     username = forms.CharField(
#         label="Your Name",
#         max_length=100,
#         error_messages={
#             "required": "Please enter your name",
#             "max_length": "Your name is too long",
#         },
#     )
#     review_text = forms.CharField(
#         label="Your Review",
#         widget=forms.Textarea,
#         max_length=300,
#         error_messages={
#             "max_length": "Your review is too long",
#         },
#     )
#     rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["username", "review_text", "rating"]
        labels = {
            "username": "Your Name",
            "review_text": "Your Review",
            "rating": "Rating",
        }
        error_messages = {
            "username": {
                "required": "Please enter your name",
                "max_length": "Your name is too long",
            },
            "review_text": {"max_length": "Your review is too long"},
            "rating": {"min_value": "Rating must be between 1 and 5"},
        }
