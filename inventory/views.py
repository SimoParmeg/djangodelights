from django.shortcuts import render, redirect
from .models import MenuItem, RecipeRequirement, Ingredient, Purchase
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Sum
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = self.request.user
        context["recipe_requirements"] = RecipeRequirement.objects.all()
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context


class SignUp(CreateView):
   form_class = UserCreationForm
   success_url = reverse_lazy('login')
   template_name = 'registration/signup.html'


class IngredientsView(LoginRequiredMixin, ListView):
    template_name = "inventory/ingredients.html"
    model = Ingredient


class UpdateIngredientView(LoginRequiredMixin, UpdateView):
    template_name = "inventory/update_ingredients.html"
    model = Ingredient
    form_class = IngredientForm


class AddIngredientView(LoginRequiredMixin, CreateView):
    template_name = "inventory/add_ingredient.html"
    model = Ingredient
    form_class = IngredientForm


class DeleteIngredientView(LoginRequiredMixin, DeleteView):
    template_name = "inventory/delete_ingredients.html"
    model = Ingredient
    success_url = reverse_lazy('ingredients')


class MenuItemView(LoginRequiredMixin, ListView):
    template_name = "inventory/menu_items.html"
    model = MenuItem


class AddMenuItemView(LoginRequiredMixin, CreateView):
    template_name = "inventory/add_menu_items.html"
    model = MenuItem
    form_class = MenuItemForm


class AddRecipeRequirements(LoginRequiredMixin, CreateView):
    template_name = "inventory/add_recipe_requirements.html"
    model = RecipeRequirement
    form_class = RecipeRequirementForm


class PurchaseView(LoginRequiredMixin, ListView):
    template_name = "inventory/purchases.html"
    model = Purchase


class AddPurchaseView(LoginRequiredMixin, CreateView):
    template_name = "inventory/add_purchases.html"
    model = Purchase
    form_class = PurchaseForm


class ReportView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/reports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"] = Purchase.objects.all()
        revenue = Purchase.objects.aggregate(revenue=Sum("menu_item__price"))["revenue"]
        total_cost = 0
        for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
                total_cost += recipe_requirement.ingredient.price_per_unit * recipe_requirement.quantity

        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = revenue - total_cost

        return context


def log_out(request):
    logout(request)
    return redirect("/")