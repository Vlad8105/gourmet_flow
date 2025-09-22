from django.test import TestCase
from django.urls import reverse
from catalog.models import DishType, Dish, Ingredient, Cook
from catalog.forms import DishForm


class CookModelTest(TestCase):

    def test_years_of_experience_default(self):
        cook = Cook.objects.create(username="testuser", password="testpassword")
        self.assertEqual(cook.years_of_experience, 0)

    def test_string_representation(self):
        cook = Cook.objects.create(username="testuser", password="testpassword", first_name="John", last_name="Doe", years_of_experience=5)
        expected_string = "John Doe (5)"
        self.assertEqual(str(cook), expected_string)


class DishListViewTest(TestCase):

    def setUp(self):
        self.dish_type = DishType.objects.create(name="Appetizer")
        self.dish = Dish.objects.create(name="Test Dish", price=15.00, dish_type=self.dish_type)
        self.ingredient = Ingredient.objects.create(name="Test Ingredient")
        self.dish.ingredients.add(self.ingredient)
        self.cook = Cook.objects.create(username="testcook")
        self.dish.cooks.add(self.cook)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("catalog:dishes-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/dish_list.html")

    def test_view_displays_all_dishes(self):
        response = self.client.get(reverse("catalog:dishes-list"))
        self.assertContains(response, self.dish.name)
        self.assertContains(response, self.dish.price)


class DishFormTest(TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.ingredient = None
        self.cook = None

    def setUp(self):
        self.dish_type = DishType.objects.create(name="Main Course")
        self.cook = Cook.objects.create_user(username="testcook", password="testpassword")
        self.ingredient = Ingredient.objects.create(name="Test Ingredient")

    def test_form_is_valid(self):
        form_data = {
            "name": "Spaghetti",
            "price": 12.50,
            "dish_type": self.dish_type.pk,
            "description": "Delicious spaghetti with tomato sauce",
            "cooks": [self.cook.pk],
            "ingredients": [self.ingredient.pk]
        }
        form = DishForm(data=form_data)

        self.assertTrue(form.is_valid())
