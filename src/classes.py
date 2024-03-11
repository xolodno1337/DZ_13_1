class Category:
    """Класс для представления категорий продуктов."""
    name: str  # Название категории
    description: str  # Описание
    products: list  # Список товаров
    total_categories = 0  # Общее количество категорий
    total_unique_products = set()  # Количество уникальных продуктов

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.new_product_list = []   # Список в который добавляем продукты в нужном нам формате

        Category.total_categories += 1

    @property
    def append_product(self):
        """Метод выводит список товаров."""
        result = ''
        for product in self.new_product_list:
            result += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return result

    @append_product.setter
    def append_product(self, product):
        """Метод добавляет товар в список товаров."""
        self.new_product_list.append(product)


class Product:
    """Класс для представления продуктов"""
    name: str  # Название
    description: str  # Описание
    price: float  # Цена
    quantity: int  # Количество в наличии
    total_products = 0  # Общее количество продуктов

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        Product.total_products += 1

    @classmethod
    def new_product(cls, name, description, price, quantity):
        """Метод создает товар и возвращает объект."""
        return cls(name, description, price, quantity)

    @property
    def prices(self):
        """Метод выводит стоимость."""
        return self.price

    @prices.setter
    def prices(self, new_price):
        if new_price <= 0:
            print('Цена введена некорректная')
        else:
            self.price = new_price


cat_1 = Category('fruit', 'mmm', ['apple', 'cherry'])
pr_3 = Product('ooo', 'ppp', 100, 5 )
pr_2 = Product('Pineapple', 'red', 100, 5)
cat_1.append_product = pr_2
print(cat_1.append_product)
# pr_2.prices = 0
# print(pr_2.prices)
# pr_3.new_product('111', 'opopo', 500, 20)
# print(pr_3.new_product)
