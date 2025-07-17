class SweetShop:
    def __init__(self):
        self.sweets = []

    def add_sweet(self, sweet_id, name, category, price, quantity):
        sweet = {
            "id": sweet_id,
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity
        }
        self.sweets.append(sweet)

    def view_sweets(self):
        return self.sweets

    def delete_sweet(self, sweet_id):
        self.sweets = [s for s in self.sweets if s["id"] != sweet_id]

    def sort_sweets(self, by="name", descending=False):
        if by not in ["name", "price"]:
            raise ValueError("Can only sort by 'name' or 'price'.")
        return sorted(self.sweets, key=lambda s: s[by], reverse=descending)

    def search_sweets(self, name=None, category=None, price_range=None):
        results = self.sweets
        if name:
            results = [s for s in results if s["name"].lower() == name.lower()]
        if category:
            results = [s for s in results if s["category"].lower() == category.lower()]
        if price_range:
            min_price, max_price = price_range
            results = [s for s in results if min_price <= s["price"] <= max_price]
        return results

    def purchase_sweet(self, sweet_id, quantity):
        for sweet in self.sweets:
            if sweet["id"] == sweet_id:
                if sweet["quantity"] < quantity:
                    raise ValueError("Not enough stock available.")
                sweet["quantity"] -= quantity
                return
        raise ValueError("Sweet ID not found.")

    def restock_sweet(self, sweet_id, quantity):
        for sweet in self.sweets:
            if sweet["id"] == sweet_id:
                sweet["quantity"] += quantity
                return
        raise ValueError("Sweet ID not found.")


