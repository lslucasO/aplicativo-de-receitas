from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'nome': 'Lucas'}
    return render(request, 'global/home.html', context)