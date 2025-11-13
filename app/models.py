products = [
    {"id": 1, "name": "T-shirt DevOps", "price": 19.9},
    {"id": 2, "name": "Sweatshirt CI/CD", "price": 39.9},
    {"id": 3, "name": "Casquette Cloud", "price": 14.9}
]

_orders = []
def get_product(pid):
    for p in products:
        if p["id"] == pid:
            return p
    return None

def add_order(data):
    oid = len(_orders) + 1
    order = {
        "id": oid,
        "product_id": data.get("product_id"),
        "qty": data.get("qty", 1),
        "customer": data.get("customer", "anonymous")
    }
    _orders.append(order)
    return order
