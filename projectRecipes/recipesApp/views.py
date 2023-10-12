from django.shortcuts import render
from utils.recipesApp.factory import make_recipe
from .models import *


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    context = {'recipes': recipes}
    return render(request, 'recipesApp/pages/home.html', context)


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    context = {'recipes': recipes}
    return render(request, 'recipesApp/pages/category.html', context)


def recipe(request, id):
    context = {
        'recipe': make_recipe(),
    }
    return render(request, 'recipesApp/pages/recipes-view.html', context)