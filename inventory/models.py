from django.db import models

# Create your models here.
class Ingredient(models.Model):
    """
    Represents a single ingredient in the restaurant's inventory
    """
    name = models.CharField(max_length=200, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=200)
    price_per_unit = models.FloatField(default=0)

class MenuItem(models.Model):
  pass

class RecipeRequirement(models.Model):
  pass

class Purchase(models.Model):
  pass

