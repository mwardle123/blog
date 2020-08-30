from django.urls import path
from . import views

urlpatterns = [
    path('cv/', views.home_page, name='home'),
    path('cv/edit/', views.edit_page, name='edit'),
    path('cv/category/new/', views.category_new, name='category_new'),
    path('cv/category/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('cv/category/<pk>/remove/', views.category_remove, name='category_remove'),
    path('cv/category/<pk>/list/', views.item_list, name='item_list'),
    path('cv/category/<int:pk>/new/', views.item_new, name='item_new'),
    path('cv/item/<int:pk>/edit/', views.item_edit, name='item_edit'),
    path('cv/item/<pk>/remove/', views.item_remove, name='item_remove'),
]