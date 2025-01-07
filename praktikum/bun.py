class Bun:
    """
    Модель булочки для бургера.
    Булочке можно дать название и назначить цену.
    """

    def __init__(self, name: str, price: float):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.name = name
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price
