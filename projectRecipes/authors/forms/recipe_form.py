from django import forms
from recipesApp.models import Recipe

class AuthorRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = 'title', 'description', 'preparation_time', \
        'preparation_time_unit', 'servings_time', 'servings_time_unit','preparation_steps', 'cover',
                