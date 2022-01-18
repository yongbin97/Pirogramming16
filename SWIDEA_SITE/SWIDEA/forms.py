from dataclasses import fields
from django import forms
from .models import *

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields ="__all__"

class DevelopForm(forms.ModelForm):
    class Meta:
        model = Develop
        fields = "__all__"

        