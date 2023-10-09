from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'recipesApp/pages/home.html')

def recipes(request, id):
    return render(request, 'recipesApp/pages/recipes.html')