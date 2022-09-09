from django.urls import path, include
from . import views


urlpatterns = [
    path("logout/", views.log_out, name="logout"),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('account/login', include('django.contrib.auth.urls'), name='login'),
    path('', views.HomeView.as_view(), name='home'),
    path('ingredients/', views.IngredientsView.as_view(), name="ingredients"),
    path('ingredients/<pk>/update', views.UpdateIngredientView.as_view(), name="update_ingredient"),
    path('ingredients/<pk>/delete', views.DeleteIngredientView.as_view(), name="delete_ingredient"),
    path('ingredients/add', views.AddIngredientView.as_view(), name="add_ingredient"),
    path('menu/', views.MenuItemView.as_view(), name="menus"),
    path('menu/add', views.AddMenuItemView.as_view(), name="add_menu"),
    path('reciperequirement/add', views.AddRecipeRequirements.as_view(), name="add_recipe_requirement"),
    path('purchases/', views.PurchaseView.as_view(), name="purchases"),
    path('purchases/add', views.AddPurchaseView.as_view(), name="add_purchase"),
    path('reports/', views.ReportView.as_view(), name="reports"),
]