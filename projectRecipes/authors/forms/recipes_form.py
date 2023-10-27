from django import forms
from utils.django_forms import add_placeholder


class RecipeForm(forms.Form):
    ...
    
    def clean(self):
        ...