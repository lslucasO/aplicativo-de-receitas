from django.contrib import admin
from django.urls import path, include
from recipesApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipesApp.urls'))
]
