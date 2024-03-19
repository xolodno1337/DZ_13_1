class Category:
    """ Класс для представления категорий продуктов. """
    name: str  # Название категории
    description: str  # Описание
    products: list  # Список товаров
    total_categories = 0  # Общее количество категорий
    total_unique_products = 0  # Количество уникальных продуктов

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.total_unique_products += len(set(self.__products))
        Category.total_categories += 1

    def __repr__(self):
        """ Представление класса Category для разработчиков. """
        return f'{self.__class__.__name__}({self.name}, {self.description}, {self.products})'

    def __str__(self):
        """ Строковое отображение класса Category. """
        return f'{self.name}, количество продуктов: {self.__len__()} шт.'

    def __len__(self):
        """ Подсчет количества продуктов на складе. """
        result = 0
        for i in self.__products:
            result += i.quantity
        return result

    @property
    def products(self):
        """ Метод выводит список товаров. """
        result = ''
        for product in self.__products:
            result += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return result

    @products.setter
    def products(self, product):
        """ Метод добавляет товар в список товаров. """
        self.__products.append(product)


class Product:
    """ Класс для представления продуктов. """
    name: str  # Название
    description: str  # Описание
    price: float  # Цена
    quantity: int  # Количество в наличии
    total_products = 0  # Общее количество продуктов

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.total_products += 1

    def __repr__(self):
        """ Представление класса Product для разработчиков. """
        return f'{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})'

    def __str__(self):
        """ Строковое отображение класса Product. """
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """ Сложение продуктов, результат выполнения сложения двух продуктов равен
       сложение сумм, умноженных на количество на складе. """
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, name, description, price, quantity):
        """ Метод создает товар и возвращает объект. """
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """ Метод выводит стоимость. """
        return self.__price

    @price.setter
    def price(self, new_price):
        """ Метод, который меняет цену на новую при выполнении условия. """
        if new_price <= 0:
            print('Цена введена некорректная')
        else:
            self.__price = new_price


cat_1 = Category('fruit', 'mmm', [])

pr_3 = Product('ooo', 'ppp', 100, 5)
pr_2 = Product('Pineapple', 'red', 100, 5)
# print(pr_2.__str__())
cat_1.products = pr_2
cat_1.products = pr_3
print(len(cat_1))
# print(cat_1.products)
# print(cat_1.__str__())
# pr_2.price = -6
# print(pr_2.price)
# pr_1 = pr_2 + pr_3
# print(pr_1)
