from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('ingredients/', views.IngredientsView.as_view(), name="ingredients"),
    path('ingredients/<pk>/update', views.UpdateIngredientView.as_view(), name="update_ingredient"),
    path('ingredients/<pk>/delete', views.DeleteIngredientView.as_view(), name="delete_ingredient"),
    path('menu/', views.MenuItemView.as_view(), name="menu"),
]