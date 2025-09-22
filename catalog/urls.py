from django.urls import path, include
from .views import (
    CookListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    DishTypeListView,
    DishTypeDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    IngredientListView,
    IngredientDetailView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView, HomeView,
)

app_name = "catalog"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cooks-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cooks-create"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cooks-update"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cooks-delete"),

    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-types/<int:pk>/", DishTypeDetailView.as_view(), name="dish-type-detail"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish-types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish-types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),

    path("dishes/", DishListView.as_view(), name="dishes-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dishes-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dishes-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dishes-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dishes-delete"),

    path("ingredients/", IngredientListView.as_view(), name="ingredients-list"),
    path("ingredients/<int:pk>/", IngredientDetailView.as_view(), name="ingredients-detail"),
    path("ingredients/create/", IngredientCreateView.as_view(), name="ingredients-create"),
    path("ingredients/<int:pk>/update/", IngredientUpdateView.as_view(), name="ingredients-update"),
    path("ingredients/<int:pk>/delete/", IngredientDeleteView.as_view(), name="ingredients-delete"),
    path("", DishListView.as_view(), name="dishes-index"),
]
