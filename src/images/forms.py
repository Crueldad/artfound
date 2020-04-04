from django import forms
from django.forms import ModelForm
from .models import Images


class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('title', 'name', 'image')