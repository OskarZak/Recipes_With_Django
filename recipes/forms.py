from django import forms
from django.core.exceptions import ValidationError

from .models import Recipes

class RecipesForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ('title', 'ingredients', 'recipe')
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control my-5'}),
            'ingredients':forms.TextInput(attrs={'class': 'form-control my-5'}),
            'recipe':forms.Textarea(attrs={'class': 'form-control mb5'}),

        }
        labels = {
            'ingredients' : 'Write your ingredients here',
            'recipe': 'Write your recipe here:'

        }

    def clean_title(self):
        title = self.cleaned_data['title']
        return title