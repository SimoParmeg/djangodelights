from django.shortcuts import render
from .models import MenuItem, RecipeRequirement, Ingredient, Purchase
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import IngredientForm


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


class IngredientsView(LoginRequiredMixin, ListView):
    template_name = "inventory/ingredients.html"
    model = Ingredient

class UpdateIngredientView(LoginRequiredMixin, UpdateView):
    template_name = "inventory/update_ingredients.html"
    model = Ingredient
    form_class = IngredientForm

class DeleteIngredientView(LoginRequiredMixin, DeleteView):
    template_name = "inventory/delete_ingredients.html"
    model = Ingredient
    success_url = reverse_lazy('ingredients')

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