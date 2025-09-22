from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from catalog.models import Cook, Dish, Ingredient, DishType


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = (
        "username",
        "years_of_experience",
        "email", "first_name",
        "last_name", "is_staff"
    )
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("years_of_experience",)}),)
    )
    list_filter = ("years_of_experience", "is_staff", "is_superuser")
    search_fields = ("username", "email", "first_name", "last_name")


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "dish_type", "display_cooks")
    list_filter = ("dish_type", "cooks")
    search_fields = ("name", "description")
    filter_horizontal = ("cooks", "ingredients")

    def display_cooks(self, obj):
        return ", ".join([cook.username for cook in obj.cooks.all()])

    display_cooks.short_description = "Cooks"


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
