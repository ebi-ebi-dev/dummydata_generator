from django import forms
from .models import Post

class DocumentForm(forms.Form):
    document = forms.FileField()
    class Meta:
        model = Post
        fields = ['document']