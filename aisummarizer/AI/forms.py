from django.forms import ModelForm
from .models import Document


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ["Context"]
        labels = {"Context": "Search book to summarize"}
