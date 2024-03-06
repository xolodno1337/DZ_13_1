import pytest
from pythonProject.src.classes import Category, Product


def test_total_categories():
    cat_1 = Category('Фрукты', 'Семечковые', ['Абрикос' 'Вишня' 'Яблоко' 'Слива'])
    cat_2 = Category('Фрукты', 'Ягоды', ['Виноград', 'Клубника', 'Крыжовник'])
    assert Category.total_categories == 2


def test_total_products():
    prod_1 = Product('Яблоко', 'Голден Делишес', 200.5, 10)
    prod_2 = Product('Персик', 'Редхейвен', 700, 5)
    assert Product.total_products == 2


@pytest.fixture()
def category_fruits():
    return Category('Фрукты', 'Семечковые', ['Абрикос' 'Вишня' 'Яблоко' 'Слива'])


def test_init_category(category_fruits):
    assert category_fruits.name == 'Фрукты'
    assert category_fruits.description == 'Семечковые'
    assert category_fruits.products == ['Абрикос' 'Вишня' 'Яблоко' 'Слива']


@pytest.fixture()
def product_apple():
    return Product('Яблоко', 'Голден Делишес', 200.5, 10)


def test_init_product(product_apple):
    assert product_apple.name == 'Яблоко'
    assert product_apple.description == 'Голден Делишес'
    assert product_apple.price == 200.5
    assert product_apple.quantity == 10
