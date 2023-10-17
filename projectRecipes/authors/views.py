from django.shortcuts import render
from .forms import RegisterForm

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