from django.shortcuts import render
from .forms import RegisterForm

def register_view(request):
    form = RegisterForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'authors/pages/register.html', context)