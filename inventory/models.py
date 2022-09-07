from django.db import models

# Create your models here.
class Ingredient(models.Model):
  name = ''
  quantity = ''
  unit = ''
  unit_price = ''

class MenuItem(models.Model):
  pass

class RecipeRequirement(models.Model):
  pass

class Purchase(models.Model):
  pass

