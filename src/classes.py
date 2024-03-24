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
        if isinstance(product, Product):
            self.__products.append(product)


class Product:
    """ Класс для представления продуктов. """
    name: str  # Название
    description: str  # Описание
    price: float  # Цена
    quantity: int  # Количество в наличии
    color: str  # Цвет
    total_products = 0  # Общее количество продуктов

    def __init__(self, name, description, price, quantity, color):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color

        Product.total_products += 1

    def __repr__(self):
        """ Представление класса Product для разработчиков. """
        return f'{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})'

    def __str__(self):
        """ Строковое отображение класса Product. """
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """ Сложение продуктов из одинаковых классов, результат выполнения сложения двух продуктов равен
       сложение сумм, умноженных на количество на складе. """
        if isinstance(other, type(self)):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError

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


class Smartphone(Product):
    """ Класс для представления Смартфона. """
    efficiency: float  # Производительность
    model: str  # Модель
    built_in_memory: int  # Объем встроенной памяти

    def __init__(self,  name, description, price, quantity, color, efficiency, model, built_in_memory):
        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.built_in_memory = built_in_memory


class LawnGrass(Product):
    """ Класс для представления травы газонной. """
    manufacturer_country: str  # Страна-производитель
    germination_period: float  # Срок прорастания

    def __init__(self, name, description, price, quantity, color, manufacturer_country, germination_period):
        super().__init__(name, description, price, quantity, color)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period


cat_1 = Category('fruit', 'mmm', [])

pr_3 = Product('ooo', 'ppp', 100, 5, 'red')
pr_2 = Product('Pineapple', 'red', 100, 5, 'blue')
pr_4 = Smartphone('iphone', 'sss', 1000, 5, 'red', 12, 'xr', 12)
# print(pr_2.__str__())
cat_1.products = pr_2
cat_1.products = pr_3
print(len(cat_1))
# print(cat_1.products)
# print(cat_1.__str__())
# pr_2.price = -6
# print(pr_2.price)
pr_1 = pr_2 + pr_4
print(pr_1)
