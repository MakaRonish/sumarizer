from django.shortcuts import render
from .forms import DocumentForm
from .function import summarizerAI
import os
from django.http import StreamingHttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Document

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Create your views here.


@login_required(login_url=reverse_lazy("logon"))
def landingpage(request):
    form = DocumentForm()
    summary = "Welcome to Book Summarizer!\n\nThis app helps you quickly understand any book by generating a clear and concise summary. To get started, simply type the title of the book you want summarized into the text field on the homepage. Whether it's a novel, biography, or non-fiction, our AI will fetch and process key ideas from the book and present a summarized version in seconds.\n \nOnce you enter the book name, click the “Summarize” button. In just a moment, the summary will appear below, highlighting the core themes, important events, and takeaways. It's a great tool for students, readers, or anyone short on time who still wants to grasp the essence of a book."
    try:
        history = Document.objects.filter(owner=request.user)
    except Document.DoesNotExist:
        history = None

    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():

            data = form.save(commit=False)
            data.owner = request.user
            summary = summarizerAI(data.Context)
            data.summary = summary
            data.save()

        # summary = summary.replace("*", "")

    context = {"DocumentForm": form, "summary": summary, "history": history}
    return render(request, "AI/landing.html", context=context)


@login_required(login_url=reverse_lazy("logon"))
def history(request, pk):
    history = Document.objects.filter(id=pk)
    context = {"history": history}
    return render(request, "AI/history.html", context)
