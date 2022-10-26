from django import forms
from django.forms import ModelForm
from .models import Post

class ManualForm(forms.ModelForm):  
    class Meta:  
        model = Post
        fields = "__all__" 