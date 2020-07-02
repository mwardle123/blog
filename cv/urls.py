from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('edit/', views.edit_page, name='edit'),
    path('category/<int:pk>/', views.add_item, name='add_item'),
    path('category/new/', views.category_new, name='category_new'),
]