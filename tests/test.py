import pytest
from pythonProject.src.classes import Category, Product


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
