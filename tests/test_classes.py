import pytest
from pythonProject.src.classes import Category, Product, Smartphone, LawnGrass


def test_total_categories():
    """ Тест на общее количество категорий. """
    Category.total_categories = 0
    cat_1 = Category('Фрукты', 'Семечковые', ['Абрикос' 'Вишня' 'Яблоко' 'Слива'])
    cat_2 = Category('Фрукты', 'Ягоды', ['Виноград', 'Клубника', 'Крыжовник'])
    assert Category.total_categories == 2


def test_total_products():
    """ Тест на общее количество продуктов. """
    Product.total_products = 0
    prod_1 = Product('Яблоко', 'Голден Делишес', 200.5, 10, 'Зеленое')
    prod_2 = Product('Персик', 'Редхейвен', 700, 5, 'Оранжевый')
    assert Product.total_products == 2


@pytest.fixture()
def category_fruits():
    return Category('Фрукты', 'Семечковые', [Product('Яблоко', 'Голден Делишес', 200.5, 10, 'Зеленое')])


def test_init_category(category_fruits):
    """ Тест на инициализацию класса Category. """
    assert category_fruits.name == 'Фрукты'
    assert category_fruits.description == 'Семечковые'
    assert category_fruits.products == 'Яблоко, 200.5 руб. Остаток: 10 шт.\n'


@pytest.fixture()
def product_apple():
    return Product('Яблоко', 'Голден Делишес', 200.5, 10, 'Зеленое')


def test_init_product(product_apple):
    """ Тест на инициализацию класса Product. """
    assert product_apple.name == 'Яблоко'
    assert product_apple.description == 'Голден Делишес'
    assert product_apple.price == 200.5
    assert product_apple.quantity == 10
    assert product_apple.color == 'Зеленое'


def test_len():
    """ Тест на подсчет количества продуктов на складе. """
    cat_1 = Category('Фрукты', 'Семечковые', [])
    prod_1 = Product('Яблоко', 'Голден Делишес', 200.5, 10, 'Зеленое')
    prod_2 = Product('Персик', 'Редхейвен', 700, 5, 'Оранжевый')
    cat_1.products = prod_1
    cat_1.products = prod_2
    assert len(cat_1) == 15


def test_add():
    """ Тест сложение продуктов. """
    prod_1 = Product('Яблоко', 'Голден Делишес', 200.5, 10, 'Зеленое')
    prod_2 = Product('Персик', 'Редхейвен', 700, 5, 'Оранжевый')
    assert prod_1 + prod_2 == 5505


def test_add_type():
    """ Тест на сложение разных типов классов. """
    prod_1 = Smartphone('Iphone', 'Pro max', 10000, 5, 'Blue', 60, '15', 512)
    prod_2 = Product('Дыня', 'Торпеда', 800, 10, 'Желтый')
    with pytest.raises(TypeError):
        prod_1 + prod_2

