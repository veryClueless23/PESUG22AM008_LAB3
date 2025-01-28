
from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data):
        """
        Converts a dictionary into a Product instance.
        """
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products():
    """
    Fetches all products from the database and returns them as a list of Product instances.
    """
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int):
    """
    Fetches a product by its ID. If not found, raises an error.
    """
    product_data = dao.get_product(product_id)
    if product_data is None:
        raise ValueError(f"Product with ID {product_id} not found.")
    return Product.load(product_data)


def add_product(product):
    """
    Adds a new product to the database.
    """
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """
    Updates the quantity of a product. Ensures the quantity is not negative.
    """
    if qty < 0:
        raise ValueError("Quantity cannot be negative.")
    dao.update_qty(product_id, qty)
