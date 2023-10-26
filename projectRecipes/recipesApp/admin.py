from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    ...
    

class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'created_at',
        'is_published',
        'author'
    ]
    
    list_display_links = [
        'title',
        'created_at'
    ]
    
    search_fields = [
        'id',
        'title',
        'description',
        'created_at',
        'slug'
    ]
    
    
    list_filter = [
        'category',
        'author',
        'is_published',
        'preparation_steps_is_html'
    ]
        
    
    list_per_page = 10
    
    list_editable = [
        'is_published'
    ]
    
    ordering = [
        '-id'
    ]
    
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)

