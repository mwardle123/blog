from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('edit/', views.edit_page, name='edit'),
    path('category/<int:pk>/', views.add_core_skill, name='add_core_skill'),
]