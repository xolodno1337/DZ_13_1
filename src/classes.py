class Category:
    """Класс для представления категорий продуктов."""
    name: str  # Название категории
    description: str  # Описание
    products: list  # Список товаров
    total_categories = 0  # Общее количество категорий
    total_unique_products = 0  # Количество уникальных продуктов

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.total_unique_products += len(self.__products)
        Category.total_categories += 1

    @property
    def products(self):
        """Метод выводит список товаров."""
        result = ''
        for product in self.__products:
            result += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return result

    @products.setter
    def products(self, product):
        """Метод добавляет товар в список товаров."""
        self.__products.append(product)


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
    def price(self):
        """Метод выводит стоимость."""
        return self.price

    @price.setter
    def price(self, new_price):
        """Метод, который меняет цену на новую при выполнении условия."""
        if new_price <= 0:
            print('Цена введена некорректная')
        else:
            self.price = new_price


cat_1 = Category('fruit', 'mmm', ['apple', 'cherry'])
pr_3 = Product('ooo', 'ppp', 100, 5)
pr_2 = Product('Pineapple', 'red', 100, 5)
cat_1.products = pr_2
# cat_1.products = pr_3
print(cat_1.products)
# pr_2.prices = 0
# print(pr_2.prices)
