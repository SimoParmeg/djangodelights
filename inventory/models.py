from django.db import models

# Create your models here.
class Ingredient(models.Model):
    """
    Represents a single ingredient in the restaurant's inventory
    """
    name = models.CharField(max_length=200, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=200)
    price_per_unit = models.FloatField(default=0.00)

class MenuItem(models.Model):
    """
    Represents an entry in the restaurant's menu
    """
    title = models.CharField(max_length=200, unique=True)
    price = models.FloatField(default=0.00)

class RecipeRequirement(models.Model):
    """
    Represents an ingredient required for a recipe for a MenuItem
    """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.00)

class Purchase(models.Model):
    """
    Represents a purchase of a MenuItem
    """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)