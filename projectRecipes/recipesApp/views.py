from django.shortcuts import render
from utils.recipesApp.factory import make_recipe
from .models import *


def home(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipesApp/pages/home.html', context)

def recipe(request, id):
    context = {
        'recipe': make_recipe(),
    }
    return render(request, 'recipesApp/pages/recipes-view.html', context)