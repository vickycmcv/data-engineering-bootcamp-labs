# Lab 1: Hello Data Engineering (print & comments)

# Python is used for data pipelines, ETL and automation
print("Welcome to Data Engineering with Python")

# Lab 2: Execution Flow with print statements
print("Step 1: Read data")
print("Step 2: Clean data")
print("Step 3: Write data")

# Lab 3: Variables and assignment
customer_name = "Asha Patel"
customer_id = 101
active = True
print(f"Customer {customer_id}: {customer_name} (Active: {active})")

# Lab 4: Data types (int, float, str, bool)
quantity = 250
price= 99.95
city = "Mumbai"
completed = False

print(f"Value: {quantity}, Type:", type(quantity))
print(f"Value: {price}, Type:", type(price))
print(f"Value: {city}, Type:", type(city))
print(f"Value: {completed}, Type:", type(completed))

# Lab 5: Type casting (int(), float(), str())
mark1 = "78"
mark2 = "85.5"

total_marks = float(mark1)+float(mark2)
print(f"Total marks: {total_marks}")

# Lab 6: Billing calculator (arithmetic, monetary formatting)
item_price = 249.99
quantity = 3
tax_rate = 0.05 # 5%

subtotal = item_price * quantity
tax = subtotal * tax_rate
grand_total = subtotal + tax

print(f"Grand Total: {grand_total:.2f}")

# Lab 7: Comparison operators
order1 = 1200
order2 = 999

print(f"Is order1 > order2? {order1 > order2}")
print(f"Are order1 and order 2 equal? {order1 == order2}")

# Lab 8: Logical operators
price = 1500
in_stock = True

print(f"High value and available? {price>1000 & in_stock}")
print(f"High value or out of stock? {price>1000 | in_stock}")

# Lab 9: Input and output (input(), print())
name=input("Enter customer name:")
amount=float(input("Enter purchase amount:"))

print(f"Receipt -- Customer: {name}, Amount: {amount:.2f}")

# Lab 10: f-strings and formatted output
product = "SSD"
price = 12999.5
qty = 2

print(f"Order: {qty} x {product} @ {price} each -- Total: {qty*price:.2f}")

# Lab 11: Basic debugging — identify and fix errors
name = "Neha"
print(name)  # typo

age = int("30")
print(f"Age next year: {age + 1}")

value = "123"
num = int(value)
print(num)

# Lab 12: Marks percentage calculator (optional preview: simple if/else)
m1 = "78"
m2 = "85"
m3 = "69"

percentage= (int(m1)+int(m2)+int(m3))*100/300
print(f"Percentage: {percentage:.2f}")
if percentage >=35:
    print("Result: Pass")
else:
    print("Result Fail")

# Lab 13: Discount calculation and rounding
original_price = 4999.99
discount_percent = 12.5

discount_amount = original_price * (discount_percent / 100)
final_price = original_price - discount_amount

print(f"Discount: {discount_amount:.2f}")
print(f"Final price: {final_price:.2f}")

# Lab 14: Final Integrated Lab: Student profile + billing (no loops/functions)

name = "Rohan Verma"
id = "205" # string intentionally
item = "Textbook"
unit_price = "450.5" # string intentionally
quantity = "2" # string intentionally

subtotal= float(unit_price)*int(quantity)
tax = subtotal*0.05# 5% of subtotal
grand_total= subtotal + tax

print(f"Customer ID: {id}")
print(f"Customer Name: {name}")
print(f"Item: {item}")
print(f"Quantity: {quantity}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Tax (5%): {tax:.2f}")
print(f"Grand Total: {grand_total:.2f}")




