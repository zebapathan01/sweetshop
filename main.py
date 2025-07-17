# main.py

from sweet_shop import SweetShop

def print_menu():
    print("""
======= Sweet Shop Menu =======
1. Add Sweet
2. View Sweets
3. Delete Sweet
4. Purchase Sweet
5. Restock Sweet
6. Search Sweet
7. Sort Sweets
0. Exit
""")


def display_sweets(sweets):
    if not sweets:
        print("No sweets found.")
        return
    print("\n📋 Current Sweets:\n")
    for s in sweets:
        print(f"{s['id']} | {s['name']} | {s['category']} | ₹{s['price']} | Qty: {s['quantity']}")
    print()


if __name__ == "__main__":
    shop = SweetShop()

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            sweet_id = input("Enter Sweet ID: ")
            name = input("Enter Sweet Name: ")
            category = input("Enter Category: ")
            price = int(input("Enter Price: "))
            quantity = int(input("Enter Quantity: "))
            shop.add_sweet(sweet_id, name, category, price, quantity)
            print("✅ Sweet added successfully.\n")

        elif choice == "2":
            display_sweets(shop.view_sweets())

        elif choice == "3":
            sweet_id = input("Enter ID to delete: ")
            shop.delete_sweet(sweet_id)
            print("🗑️ Sweet deleted.\n")

        elif choice == "4":
            sweet_id = input("Enter ID to purchase: ")
            quantity = int(input("Enter quantity: "))
            try:
                shop.purchase_sweet(sweet_id, quantity)
                print("🛒 Purchase successful.\n")
            except ValueError as e:
                print(f"❌ {e}\n")

        elif choice == "5":
            sweet_id = input("Enter ID to restock: ")
            quantity = int(input("Enter quantity: "))
            try:
                shop.restock_sweet(sweet_id, quantity)
                print("🔁 Restocked successfully.\n")
            except ValueError as e:
                print(f"❌ {e}\n")

        elif choice == "6":
            print("Search by: 1. Name  2. Category  3. Price Range")
            opt = input("Enter option: ").strip()
            if opt == "1":
                name = input("Enter sweet name: ")
                results = shop.search_sweets(name=name)
            elif opt == "2":
                category = input("Enter category: ")
                results = shop.search_sweets(category=category)
            elif opt == "3":
                min_p = int(input("Min price: "))
                max_p = int(input("Max price: "))
                results = shop.search_sweets(price_range=(min_p, max_p))
            else:
                print("❌ Invalid option\n")
                continue
            display_sweets(results)

        elif choice == "7":
            sort_by = input("Sort by 'name' or 'price': ").strip()
            order = input("Descending? (yes/no): ").strip().lower() == "yes"
            try:
                results = shop.sort_sweets(by=sort_by, descending=order)
                display_sweets(results)
            except ValueError as e:
                print(f"❌ {e}\n")

        elif choice == "0":
            print("👋 Exiting Sweet Shop. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.\n")
