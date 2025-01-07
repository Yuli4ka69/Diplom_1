import pytest
from praktikum.database import Database
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def db():
    """Fixture для создания объекта Database."""
    return Database()


def test_burger_creation(db):
    """Тестирование создания бургера."""
    burger = Burger()

    buns = db.available_buns()
    ingredients = db.available_ingredients()

    # Добавляем булочку и ингредиенты
    burger.set_buns(buns[0])  # Черная булочка
    burger.add_ingredient(ingredients[1])  # Сметана
    burger.add_ingredient(ingredients[4])  # Динозавр
    burger.add_ingredient(ingredients[3])  # Котлета
    burger.add_ingredient(ingredients[5])  # Колбаса

    # Проверяем, что булочка и ингредиенты добавлены
    assert burger.bun.get_name() == "black bun"
    assert len(burger.ingredients) == 4
    assert burger.ingredients[0].get_name() == "sour cream"
    assert burger.ingredients[1].get_name() == "dinosaur"
    assert burger.ingredients[2].get_name() == "cutlet"
    assert burger.ingredients[3].get_name() == "sausage"


def test_move_ingredient(db):
    """Тестирование перемещения ингредиента."""
    burger = Burger()

    buns = db.available_buns()
    ingredients = db.available_ingredients()

    # Добавляем булочку и ингредиенты
    burger.set_buns(buns[0])
    burger.add_ingredient(ingredients[1])  # Сметана
    burger.add_ingredient(ingredients[4])  # Динозавр

    # Перемещаем ингредиент
    burger.move_ingredient(1, 0)

    # Проверяем, что ингредиенты перемещены
    assert burger.ingredients[0].get_name() == "dinosaur"
    assert burger.ingredients[1].get_name() == "sour cream"


def test_remove_ingredient():
    burger = Burger()
    ingredient = Ingredient(name="sour cream", price=2.5, ingredient_type="sauce")  # Реальный объект
    burger.add_ingredient(ingredient)

    burger.remove_ingredient(0)

    assert len(burger.ingredients) == 0


def test_get_receipt(db):
    """Тестирование получения рецепта бургера."""
    burger = Burger()

    buns = db.available_buns()
    ingredients = db.available_ingredients()

    # Собираем бургер
    burger.set_buns(buns[0])  # Черная булочка
    burger.add_ingredient(ingredients[1])  # Сметана
    burger.add_ingredient(ingredients[4])  # Динозавр
    burger.add_ingredient(ingredients[3])  # Котлета

    # Получаем рецепт
    receipt = burger.get_receipt()

    # Проверяем, что рецепт соответствует ожиданиям
    assert "black bun" in receipt
    assert "sour cream" in receipt
    assert "dinosaur" in receipt
    assert "cutlet" in receipt
