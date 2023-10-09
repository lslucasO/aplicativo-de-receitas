from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'recipesApp/pages/home.html')

def recipe(request):
    return render(request, 'recipesApp/pages/recipe.html')