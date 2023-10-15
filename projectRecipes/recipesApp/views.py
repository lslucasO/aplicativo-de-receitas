from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.db.models import Q
from utils.recipesApp.factory import make_recipe
from django.core.paginator import Paginator
from django.http import Http404
from .models import *


def home(request):
 
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    
    
    paginator = Paginator(recipes, 9)
    page_object = paginator.get_page(1)
    
    context = {'recipes': page_object,
               'page_title': 'Home'
    }
    return render(request, 'recipesApp/pages/home.html', context)


def category(request, category_id):

    recipes = get_list_or_404(
        Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    )
     
    context = {'recipes': recipes,
               'page_title': f'{recipes[0].category.name}'
    }
    return render(request, 'recipesApp/pages/category.html', context)


def search(request):
    search_term = request.GET.get('q', '').strip()
    
    if not search_term:
        raise Http404()
       
    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term)
        ),
        is_published = True
    ).order_by('-id')   
    
    context = {
        'search_term': search_term,
        'page_title': f'Search for "{search_term}"',
        'recipes': recipes
    }
    
    return render(request, 'recipesApp/pages/search.html', context)


def recipe(request, id):
    
    recipes = get_object_or_404(
        Recipe, 
        pk = id,
        is_published=True,
    )
    
    context = {
        'recipe': recipes,
    }
    return render(request, 'recipesApp/pages/recipes-view.html', context)