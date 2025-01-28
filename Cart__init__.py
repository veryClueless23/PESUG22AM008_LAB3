import json
from typing import List
from cart import dao
from products import Product, get_product


class Cart:
    def __init__(self, id: int, username: str, contents: List[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data: dict) -> 'Cart':
        return Cart(
            id=data['id'],
            username=data['username'],
            contents=[get_product(product_id) for product_id in json.loads(data['contents'])],
            cost=data['cost']
        )


def get_cart(username: str) -> List[Product]:
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    items = []
    for cart_detail in cart_details:
        # Safely parse JSON instead of using eval
        product_ids = json.loads(cart_detail['contents'])
        items.extend(get_product(product_id) for product_id in product_ids)

    return items


def add_to_cart(username: str, product_id: int) -> None:
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int) -> None:
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str) -> None:
    dao.delete_cart(username)

