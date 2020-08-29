from django.urls import path
from . import views

urlpatterns = [
    path('cv/', views.home_page, name='home'),
    path('cv/edit/', views.edit_page, name='edit'),
    path('cv/category/<int:pk>/', views.add_item, name='add_item'),
    path('cv/category/new/', views.category_new, name='category_new'),
    path('cv/category/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('cv/category/<pk>/remove/', views.category_remove, name='category_remove'),
]