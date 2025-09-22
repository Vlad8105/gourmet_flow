from django.contrib.auth.models import AbstractUser
from django.db import models


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0)
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="cooks",
        related_query_name="cook",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="cooks",
        related_query_name="cook",
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.years_of_experience})"


class DishType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name="dishes")
    cooks = models.ManyToManyField(Cook, related_name="dishes")
    ingredients = models.ManyToManyField("Ingredient", related_name="dishes")

    def __str__(self):
        if self.dish_type:
            return f"{self.dish_type.name} {self.name}"
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
