from datetime import date
from django.utils import timezone

from myapp.models import Request, Comment
from django import forms

class MyForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('name', 'phone', 'date', 'message')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'message', 'date')