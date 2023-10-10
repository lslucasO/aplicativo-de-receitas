from django.shortcuts import render
from utils.recipesApp.factory import make_recipe
# Create your views here.
def home(request):
    context = {
        'recipes': [make_recipe() for _ in range(9)],
    }
    return render(request, 'recipesApp/pages/home.html', context)

def recipe(request, id):
    context = {
        'recipe': make_recipe(),
    }
    return render(request, 'recipesApp/pages/recipes-view.html', context)