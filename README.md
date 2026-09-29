README
Shopping and Billing System
A simple console application in Python for adding products to a cart and generating a bill with
discount and GST.
Features
• Display the product list (10 products)
• Add a product to the cart with a quantity
• View the cart with line totals and subtotal
• Generate a final bill: 5% discount from Rs. 500, 10% discount from Rs. 1000, then 5% GST
• Messages for an empty cart, invalid product number and invalid menu choice
Requirements
• Python 3.6 or higher
• No external libraries needed
How to Run
• 1. Extract the zip and open a terminal in the folder.
• 2. Run: python shopping_billing_system.py
• 3. Follow the on-screen menu.
Menu Options
Option Action
1 Display Products
2 Add Product to Cart
3 View Cart
4 Generate Bill
5 Exit
Page | 1
Shopping and Billing System README
Sample Usage
Enter your choice: 2
(product list is shown)
Enter product number: 1
Enter quantity: 5
Product added to cart!
Enter your choice: 4
Subtotal : Rs. 300
Discount : Rs. 0
GST (5%) : Rs. 15.0
Final Amount : Rs. 315.0
Notes
• Data is stored in memory and is not saved after exit.
• Entering non-numeric text for a product number or quantity will raise an error (see Report for
suggested improvements).
• Quantities are not checked, so a negative quantity is accepted.
Files
• 1_Statement.pdf - problem statement
• 2_ReadMe.pdf - this file
• 3_Report.pdf - project report
• 4_Code.pdf - source code listing
• shopping_billing_system.py - runnable source file
