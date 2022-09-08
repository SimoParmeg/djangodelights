from django.db import models


class Ingredient(models.Model):
    """
    Represents a single ingredient in the restaurant's inventory
    """
    name = models.CharField(max_length=200, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=200)
    price_per_unit = models.FloatField(default=0.00)

    def get_absolute_url(self):
        return "/ingredients"

    def __str__(self):
        return f"""
        name: {self.name};
        quantity: {self.quantity};
        unit: {self.unit};
        price_per_unit: {self.price_per_unit}
        """


class MenuItem(models.Model):
    """
    Represents an entry in the restaurant's menu
    """
    title = models.CharField(max_length=200, unique=True)
    price = models.FloatField(default=0.00)

    def get_absolute_url(self):
        return "/menu"

    def __str__(self):
        return f"""title: {self.title}; price: {self.price}"""


class RecipeRequirement(models.Model):
    """
    Represents an ingredient required for a recipe for a MenuItem
    """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.00)

    def get_absolute_url(self):
        return "/purchases"

    def __str__(self):
        return f"menu_item: {self.menu_item.title}; ingredients: {self.ingredient.name}; quantity: {self.quantity}"

    def is_enough(self):
        """return `True` if the ingredient quantity available meet the recipe's requirements"""
        return self.ingredient.quantity >= self.quantity


class Purchase(models.Model):
    """
    Represents a purchase of a MenuItem
    """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return "/purchases"

    def __str__(self):
        return f"menu_item: {self.menu_item.title}; time: {self.timestamp}"