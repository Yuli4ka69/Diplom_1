import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
@pytest.fixture
def ingredient():
    """Fixture для создания объекта Ingredient."""
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

def test_get_name(ingredient):
    """Тестирование метода get_name."""
    assert ingredient.get_name() == "hot sauce"

def test_get_price(ingredient):
    """Тестирование метода get_price."""
    assert ingredient.get_price() == 100

def test_get_type(ingredient):
    """Тестирование метода get_type."""
    assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
