import pytest
from praktikum.bun import Bun

# Проверка корректной инициализации
@pytest.mark.parametrize(
    "name, price, expected_name, expected_price",
    [
        ("Sesame", 1.5, "Sesame", 1.5),
        ("Brioche", 2.0, "Brioche", 2.0),
        ("Whole Wheat", 1.8, "Whole Wheat", 1.8),
    ],
)
def test_bun_initialization(name, price, expected_name, expected_price):
    bun = Bun(name, price)
    assert bun.get_name() == expected_name
    assert bun.get_price() == expected_price

# Проверка возврата имени
def test_bun_get_name():
    bun = Bun("Rye", 1.7)
    assert bun.get_name() == "Rye"

# Проверка возврата цены
def test_bun_get_price():
    bun = Bun("Multigrain", 2.5)
    assert bun.get_price() == 2.5
