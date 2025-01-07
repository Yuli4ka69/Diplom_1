from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


def test_set_buns():
    burger = Burger()
    mock_bun = Mock(spec=Bun)
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun


def test_add_ingredient():
    burger = Burger()
    mock_ingredient = Mock(spec=Ingredient)
    burger.add_ingredient(mock_ingredient)
    assert mock_ingredient in burger.ingredients


def test_remove_ingredient():
    burger = Burger()
    mock_ingredient = Mock(spec=Ingredient)
    burger.add_ingredient(mock_ingredient)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0


def test_move_ingredient():
    burger = Burger()
    ingredient1 = Mock(spec=Ingredient)
    ingredient2 = Mock(spec=Ingredient)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    # Move ingredient2 to the first position
    burger.move_ingredient(1, 0)
    assert burger.ingredients == [ingredient2, ingredient1]


def test_get_price():
    burger = Burger()
    mock_bun = Mock(spec=Bun)
    mock_bun.get_price.return_value = 2.0
    burger.set_buns(mock_bun)

    ingredient1 = Mock(spec=Ingredient)
    ingredient1.get_price.return_value = 1.5
    ingredient2 = Mock(spec=Ingredient)
    ingredient2.get_price.return_value = 2.0

    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    # Expected price: 2 * bun price + ingredient prices
    expected_price = 2.0 * 2 + 1.5 + 2.0
    assert burger.get_price() == expected_price


def test_get_receipt():
    burger = Burger()
    mock_bun = Mock(spec=Bun)
    mock_bun.get_name.return_value = "Sesame"
    mock_bun.get_price.return_value = 1.5
    burger.set_buns(mock_bun)

    mock_ingredient = Mock(spec=Ingredient)
    mock_ingredient.get_name.return_value = "Lettuce"
    mock_ingredient.get_type.return_value = "Filling"
    mock_ingredient.get_price.return_value = 0.5

    burger.add_ingredient(mock_ingredient)

    # Expected receipt
    expected_receipt = (
        "(==== Sesame ====)\n"
        "= filling Lettuce =\n"
        "(==== Sesame ====)\n"
        "Price: 3.5"
    )
    assert burger.get_receipt() == expected_receipt
