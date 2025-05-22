inventory = []

def add_item(item_name, quantity):
    inventory.append({"name": item_name, "quantity": quantity})
    print(f"Added {quantity} {item_name}(s) to inventory.")

def display_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for item in inventory:
            print(f"- {item['name']}: {item['quantity']} units")

def update_quantity(item_name, new_quantity):
    for item in inventory:
        if item["name"] == item_name:
            item["quantity"] = new_quantity
            print(f"Updated {item_name} to {new_quantity} units.")
            return
    print(f"{item_name} not found in inventory.")

add_item("Apple", 50)
add_item("Banana", 30)
display_inventory()
update_quantity("Apple", 60)
display_inventory()