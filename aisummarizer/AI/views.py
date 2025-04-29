from django.shortcuts import render
from .forms import DocumentForm
from .function import summarizerAI
import os
from django.http import StreamingHttpResponse

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Create your views here.


def landingpage(request):
    form = DocumentForm()
    summary = "hehe"
    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():

            data = form.save(commit=False)
            data.save()
            summary = summarizerAI(data.Context)

        # summary = summary.replace("*", "")

    context = {"DocumentForm": form, "summary": summary}
    return render(request, "AI/landing.html", context=context)


# def stream_summary(request):
#     if request.method == "POST":
#         form = DocumentForm(request.POST)
#         if form.is_valid():
#             data = form.save(commit=False)
#             data.save()

#             response = StreamingHttpResponse(
#                 summarizerAI(data.Context), content_type="text/plain"
#             )
#             return response

#     form = DocumentForm()
#     return render(request, "AI/landing.html", {"DocumentForm": form})
