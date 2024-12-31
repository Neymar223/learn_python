products = []

while True:
    choice = int(input(  
        "1.Add\n2.Remove\n3.List All Items\n4.Exit\nEnter your choice: "
    ))

    if choice == 1:
        name = input("Enter product Name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Quantity: "))
        item = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        products.append(item)
        print("Product Added")

    elif choice == 2:  # Remove
        name = input("Enter product name to remove: ")
        found = False
        for item in products:
            if item["name"] == name:
                products.remove(item)
                print("Product Deleted")
                found = True
                break
        if not found:
            print("Item not found!")

    elif choice == 3:  # List
        if products:
            for item in products:
                print(
                    f"Name: {item['name']} "
                    f"Quantity: {item['quantity']} "
                    f"Price: {item['price']} "
                    f"Total Price: {item['price'] * item['quantity']}"
                )
        else:
            print("No products available.")

    elif choice == 4:
        total_price = 0.0
        for item in products:
            total_price += item["price"] * item["quantity"]
        print(f"Your total price is: {total_price}")
        break

    else:
        print("Invalid choice, please try again.")
