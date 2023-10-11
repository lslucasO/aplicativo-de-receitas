from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from recipesApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipesApp.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)