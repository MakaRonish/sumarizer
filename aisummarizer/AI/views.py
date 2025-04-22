from django.shortcuts import render
from .forms import DocumentForm
from .function import summarizerAI

# Create your views here.


def landingpage(request):
    form = DocumentForm()
    summary = ""
    if request.method == "POST":
        form = DocumentForm(request.POST)
        data = form.save(commit=False)
        data.save()
        summary = summarizerAI(data.Context)
        summary = summary.replace("*", "")
        print(summary)

    context = {"DocumentForm": form, "summary": summary}
    return render(request, "AI/landing.html", context=context)
