from django import forms
from .models import Model

class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ['name', 'description', 'file', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }