from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.urls import reverse
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login


    
def register_view(request):
    # Pega quantas vezes o usuario acessou aquela página
    # request.session['number'] = request.session.get('number') or 1
    # request.session['number'] += 1
    
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    context = {
        'form': form,
        'form_action': reverse('register_create'),
        'page_title': 'Register'
    }
    
    return render(request, 'authors/pages/register.html', context)


def register_create(request):
    
    if not request.POST:
        raise Http404()

    POST = request.POST 
    # Salvando os dados do usuario por sessão
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)
    
    if form.is_valid():
        # Salvando usuario no banco de dados
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Your user is created, please log in.')
        
        del(request.session['register_form_data'])
    
   # Redirecionando para a view de registro
    return redirect('register')


def login_view(request):
    
    form = LoginForm()
    
    context = {
        'form': form,
        'form_action': reverse('login_create'),
        'page_title': 'Login'
    }
    
    return render(request, 'authors/pages/login.html', context)


def login_create(request):
    
    if not request.POST:
        raise Http404
    
    form = LoginForm(request.POST)
    login_url = reverse('login')
    
    
    if form.is_valid():
        is_authenticated = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )
        
        if is_authenticated is not None:
            messages.success(request, 'You are logged in.')
            return redirect(login_url)
        else:
            messages.error(request, 'Invalid credentials, please try again.')
            return redirect(login_url)
    
    else:
        messages.error(request, 'Error to validate form.')
        
    
    
    
    
    context = {
        'page_title': 'Login'
    }
    
    return render(request, 'authors/pages/login.html', context)