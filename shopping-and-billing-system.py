# Shopping and Billing System

products = {
    1: ["Rice", 60],
    2: ["Wheat", 50],
    3: ["Sugar", 45],
    4: ["Milk", 30],
    5: ["Biscuits", 25],
    6: ["Chocolate", 40],
    7: ["Soap", 35],
    8: ["Shampoo", 120],
    9: ["Juice", 50],
    10: ["Coffee", 90]
}

cart = []

def display_products():
    print("\n========== PRODUCT LIST ==========")
    for number, item in products.items():
        print(number, ".", item[0], "- Rs.", item[1])
    print("==================================")


def add_to_cart():
    display_products()

    choice = int(input("\nEnter product number: "))

    if choice in products:
        quantity = int(input("Enter quantity: "))

        name = products[choice][0]
        price = products[choice][1]
        total = price * quantity

        cart.append([name, price, quantity, total])

        print("Product added to cart!")
    else:
        print("Invalid product number.")


def show_cart():
    if len(cart) == 0:
        print("\nYour cart is empty.")
        return

    print("\n========== YOUR CART ==========")

    subtotal = 0

    for item in cart:
        print(item[0], "| Price:", item[1],
              "| Quantity:", item[2],
              "| Total:", item[3])
        subtotal += item[3]

    print("--------------------------------")
    print("Subtotal: Rs.", subtotal)


def generate_bill():
    if len(cart) == 0:
        print("\nCart is empty. Add products first.")
        return

    subtotal = 0

    print("\n================================")
    print("          FINAL BILL")
    print("================================")

    for item in cart:
        print(item[0], "x", item[2], "=", "Rs.", item[3])
        subtotal += item[3]

    if subtotal >= 1000:
        discount = subtotal * 0.10
    elif subtotal >= 500:
        discount = subtotal * 0.05
    else:
        discount = 0

    after_discount = subtotal - discount
    gst = after_discount * 0.05
    final_amount = after_discount + gst

    print("--------------------------------")
    print("Subtotal       : Rs.", round(subtotal, 2))
    print("Discount       : Rs.", round(discount, 2))
    print("GST (5%)       : Rs.", round(gst, 2))
    print("--------------------------------")
    print("Final Amount   : Rs.", round(final_amount, 2))
    print("================================")
    print("Thank you for shopping!")


while True:

    print("\n")
    print("================================")
    print("       SHOPPING & BILLING")
    print("================================")
    print("1. Display Products")
    print("2. Add Product to Cart")
    print("3. View Cart")
    print("4. Generate Bill")
    print("5. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_products()

    elif choice == "2":
        add_to_cart()

    elif choice == "3":
        show_cart()

    elif choice == "4":
        generate_bill()

    elif choice == "5":
        print("Thank you! Visit again.")
        break

    else:
        print("Invalid choice. Please try again.")
