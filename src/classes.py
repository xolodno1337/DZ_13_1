class Category:
    """Класс для представления категорий продуктов."""
    name: str
    description: str
    products: list
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.total_categories += 1


class Product:
    """Класс для представления продуктов"""
    name: str
    description: str
    price: float
    quantity: int
    total_products = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        Product.total_products += 1


# cat_1 = Category('Фрукты', 'Семечковые', ['Абрикос' 'Вишня' 'Яблоко' 'Слива'])
# cat_2 = Category('Фрукты', 'Ягоды', ['Виноград', 'Клубника', 'Крыжовник'])
# print(Category.total_categories)
# print(cat_1.name)