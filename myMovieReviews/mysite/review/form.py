from django import forms
from .models import Review

class PostForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = '__all__'