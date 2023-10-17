from django.urls import path
from  authors import views

urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('register/create/', views.register_create, name="create"),
]
