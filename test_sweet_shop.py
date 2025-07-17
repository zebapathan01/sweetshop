from sweet_shop import SweetShop
import pytest

def test_add_sweet():
    shop = SweetShop()
    shop.add_sweet("1001", "Kaju Katli", "Nut-Based", 50, 20)
    sweets = shop.view_sweets()
    assert len(sweets) == 1
    assert sweets[0]["name"] == "Kaju Katli"

def test_view_sweets():
    shop = SweetShop()
    shop.add_sweet("1002", "Gulab Jamun", "Milk-Based", 30, 10)
    shop.add_sweet("1003", "Rasgulla", "Milk-Based", 25, 15)
    sweets = shop.view_sweets()
    assert len(sweets) == 2
    assert sweets[0]["name"] == "Gulab Jamun"

def test_delete_sweet():
    shop = SweetShop()
    shop.add_sweet("1004", "Barfi", "Milk-Based", 35, 10)
    shop.add_sweet("1005", "Ladoo", "Nut-Based", 20, 15)
    shop.delete_sweet("1004")
    sweets = shop.view_sweets()
    assert len(sweets) == 1
    assert sweets[0]["name"] == "Ladoo"

def test_sort_sweets_by_name():
    shop = SweetShop()
    shop.add_sweet("1001", "Rasgulla", "Milk-Based", 25, 30)
    shop.add_sweet("1002", "Kaju Katli", "Nut-Based", 50, 20)
    shop.add_sweet("1003", "Barfi", "Milk-Based", 35, 10)
    sorted_sweets = shop.sort_sweets(by="name")
    names = [s["name"] for s in sorted_sweets]
    assert names == ["Barfi", "Kaju Katli", "Rasgulla"]

def test_sort_sweets_by_price_descending():
    shop = SweetShop()
    shop.add_sweet("1004", "Ladoo", "Nut-Based", 15, 40)
    shop.add_sweet("1005", "Peda", "Milk-Based", 30, 20)
    shop.add_sweet("1006", "Halwa", "Flour-Based", 10, 25)
    sorted_sweets = shop.sort_sweets(by="price", descending=True)
    prices = [s["price"] for s in sorted_sweets]
    assert prices == [30, 15, 10]

def test_search_by_name():
    shop = SweetShop()
    shop.add_sweet("2001", "Rasgulla", "Milk-Based", 25, 30)
    shop.add_sweet("2002", "Kaju Katli", "Nut-Based", 50, 20)
    result = shop.search_sweets(name="Rasgulla")
    assert len(result) == 1
    assert result[0]["name"] == "Rasgulla"

def test_search_by_category():
    shop = SweetShop()
    shop.add_sweet("2003", "Ladoo", "Nut-Based", 20, 15)
    shop.add_sweet("2004", "Peda", "Milk-Based", 30, 10)
    result = shop.search_sweets(category="Nut-Based")
    assert len(result) == 1
    assert result[0]["category"] == "Nut-Based"

def test_search_by_price_range():
    shop = SweetShop()
    shop.add_sweet("2005", "Halwa", "Flour-Based", 10, 25)
    shop.add_sweet("2006", "Barfi", "Milk-Based", 35, 10)
    result = shop.search_sweets(price_range=(5, 20))
    assert len(result) == 1
    assert result[0]["name"] == "Halwa"

def test_purchase_sweet_reduces_quantity():
    shop = SweetShop()
    shop.add_sweet("3001", "Kaju Katli", "Nut-Based", 50, 10)
    shop.purchase_sweet("3001", 3)
    sweets = shop.view_sweets()
    assert sweets[0]["quantity"] == 7

def test_purchase_sweet_not_enough_stock():
    shop = SweetShop()
    shop.add_sweet("3002", "Gulab Jamun", "Milk-Based", 30, 2)
    with pytest.raises(ValueError) as e:
        shop.purchase_sweet("3002", 5)
    assert str(e.value) == "Not enough stock available."

def test_restock_sweet_increases_quantity():
    shop = SweetShop()
    shop.add_sweet("4001", "Ladoo", "Nut-Based", 20, 5)
    shop.restock_sweet("4001", 10)
    sweets = shop.view_sweets()
    assert sweets[0]["quantity"] == 15

def test_restock_sweet_invalid_id():
    shop = SweetShop()
    shop.add_sweet("4002", "Peda", "Milk-Based", 25, 5)
    with pytest.raises(ValueError) as e:
        shop.restock_sweet("9999", 5)
    assert str(e.value) == "Sweet ID not found."
