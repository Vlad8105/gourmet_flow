from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView, TemplateView,
)
from .models import Cook, DishType, Dish, Ingredient
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = "catalog/home.html"


class CookListView(ListView):
    model = Cook
    template_name = "catalog/cook/cook_list.html"
    context_object_name = "cooks"


class CookDetailView(DetailView):
    model = Cook
    template_name = "catalog/cook/cook_detail.html"


class CookCreateView(CreateView):
    model = Cook
    fields = ["username", "first_name", "last_name", "years_of_experience"]
    template_name = "catalog/cook/cook_form.html"
    success_url = reverse_lazy("cooks-list")


class CookUpdateView(UpdateView):
    model = Cook
    fields = ["username", "first_name", "last_name", "years_of_experience"]
    template_name = "catalog/cook/cook_form.html"
    success_url = reverse_lazy("cooks-list")


class CookDeleteView(DeleteView):
    model = Cook
    template_name = "catalog/cook/cook_confirm_delete.html"
    success_url = reverse_lazy("cooks-list")


class DishTypeListView(ListView):
    model = DishType
    template_name = "catalog/dish_type/dish_type_list.html"
    context_object_name = "dish_types_list"


class DishTypeDetailView(DetailView):
    model = DishType
    template_name = "catalog/dish_type/dish_type_detail.html"
    context_object_name = "dish_type_list"


class DishTypeCreateView(CreateView):
    model = DishType
    fields = ["name"]
    template_name = "catalog/dish_type/dish_type_form.html"
    success_url = reverse_lazy("dish-type-list")


class DishTypeUpdateView(UpdateView):
    model = DishType
    fields = ["name"]
    template_name = "catalog/dish_type/dish_type_form.html"
    success_url = reverse_lazy("dish-type-list")


class DishTypeDeleteView(DeleteView):
    model = DishType
    template_name = "catalog/dish_type/dish_type_confirm_delete.html"
    success_url = reverse_lazy("dish-type-list")


class DishListView(ListView):
    model = Dish
    template_name = "catalog/dishes/dish_list.html"
    context_object_name = "dish_list"


class DishDetailView(DetailView):
    model = Dish
    template_name = "catalog/dishes/dish_detail.html"
    context_object_name = "dish"


class DishCreateView(CreateView):
    model = Dish
    fields = "__all__"
    template_name = "catalog/dishes/dish_form.html"
    success_url = reverse_lazy("dishes-list")


class DishUpdateView(UpdateView):
    model = Dish
    fields = "__all__"
    template_name = "catalog/dishes/dish_form.html"
    success_url = reverse_lazy("dishes-list")


class DishDeleteView(DeleteView):
    model = Dish
    template_name = "catalog/dishes/dish_confirm_delete.html"
    success_url = reverse_lazy("dishes-list")


class IngredientListView(ListView):
    model = Ingredient
    template_name = "catalog/ingredient/ingredient_list.html"
    context_object_name = "ingredients"


class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = "catalog/ingredient/ingredient_detail.html"
    context_object_name = "ingredient"


class IngredientCreateView(CreateView):
    model = Ingredient
    fields = ["name"]
    template_name = "catalog/ingredient/ingredient_form.html"
    success_url = reverse_lazy("ingredients-list")


class IngredientUpdateView(UpdateView):
    model = Ingredient
    fields = ["name"]
    template_name = "catalog/ingredient/ingredient_form.html"
    success_url = reverse_lazy("ingredients-list")


class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = "catalog/ingredient/ingredient_confirm_delete.html"
    success_url = reverse_lazy("ingredients-list")
