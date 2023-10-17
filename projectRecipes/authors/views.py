from django.shortcuts import render
from .forms import RegisterForm
from django.http import Http404
from django.contrib import messages

def register_view(request):
    
    if request.POST:
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    
    context = {
        'form': form,
        'page_title': 'Authors'
    }
    
    return render(request, 'authors/pages/register.html', context)


def register_create(request):
    
    if not request.POST:
        raise Http404()
        
    form = RegisterForm(request.POST)
    
    context = {
        'form': form,
        'page_title': 'Authors'
    }
    
    messages.success(request, "Usuario registrado com sucesso.")
    
    return render(request, 'authors/pages/register.html', context)