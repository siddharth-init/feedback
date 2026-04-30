from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm
from .models import Review

from django.views import View


# Create your views here.
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "review/feedback.html", {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        return render(request, "review/feedback.html", {"form": form})


# def review(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)

#         if form.is_valid():  # validation of form
#             # print(form.cleaned_data)
#             # review = Review(
#             #     username=form.cleaned_data["username"],
#             #     review_text=form.cleaned_data["review_text"],
#             #     rating=form.cleaned_data["rating"],
#             # )
#             # review.save()
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#     else:  # else render the form with validation error
#         form = ReviewForm()

#     return render(request, "review/feedback.html", {"form": form})


def thankyou(request):
    return render(request, "review/thankyou.html")
