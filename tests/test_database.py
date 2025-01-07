import pytest
from praktikum.database import Database
from praktikum.burger import Burger

@pytest.fixture
def db():
    """Fixture для создания объекта Database."""
    return Database()


def test_available_buns(db):
    """Тестирование метода available_buns."""
    buns = db.available_buns()

    # Проверяем, что вернутся 3 булочки
    assert len(buns) == 3
    assert buns[0].get_name() == "black bun"
    assert buns[1].get_name() == "white bun"
    assert buns[2].get_name() == "red bun"


def test_available_ingredients(db):
    """Тестирование метода available_ingredients."""
    ingredients = db.available_ingredients()

    # Проверяем, что вернутся 6 ингредиентов
    assert len(ingredients) == 6
    assert ingredients[0].get_name() == "hot sauce"
    assert ingredients[1].get_name() == "sour cream"
    assert ingredients[2].get_name() == "chili sauce"
    assert ingredients[3].get_name() == "cutlet"
    assert ingredients[4].get_name() == "dinosaur"
    assert ingredients[5].get_name() == "sausage"


def test_add_bun_to_burger(db):
    """Тестирование добавления булочки к бургеру."""
    bun = db.available_buns()[0]  # Используем черную булочку
    burger = Burger()  # создаем реальный объект Burger
    burger.set_buns(bun)

    # Проверяем, что булочка была установлена правильно
    assert burger.bun.get_name() == bun.get_name()


def test_add_ingredient_to_burger(db):
    """Тестирование добавления ингредиента к бургеру."""
    ingredient = db.available_ingredients()[0]  # Используем горячий соус
    burger = Burger()  # создаем реальный объект Burger
    burger.add_ingredient(ingredient)

    # Проверяем, что ингредиент был добавлен
    assert burger.ingredients[0].get_name() == ingredient.get_name()
