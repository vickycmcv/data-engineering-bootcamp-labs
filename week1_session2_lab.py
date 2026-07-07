# Lab 1: Pass / Fail using if
marks = 72
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# Lab 2: Grade using if / elif / else
score = 83
if score >= 90:
    print("Grade A")
elif score >= 75 and score < 90:
    print("Grade B")
elif score >= 60 and score < 75:
    print("Grade C")
elif score >= 40 and score < 60:
    print("Grade D")
else:
    print("Fail")

# Lab 3: Eligibility check with nested conditions
age = 25
has_income = True

if age >= 21:
    if has_income:
        print("Elegible for loan")
    else:
        print("Not eligible: no income")
else:
    print("Not eligible: underage")

# Lab 4: For loop over customer names
customers = ["Asha", "Ravi", "Meera"]
for customer in customers:
    print(f"Hello, {customer}!")

# Lab 5: While loop — simple counter
number = 0
while number < 5:
    number += 1
    print(number)

# Lab 6: break and continue in order processing
orders = [1500, -50, 300, 12000, 200]
for order in orders:
    if order < 0:
        continue
    elif order > 10000:
        break
    else:
        print(f"Processed: {order}")

# Lab 7: List operations — manage order IDs
order_ids = [101, 102, 104]
order_ids.insert(1,103)
order_ids.remove(102)
print(f"Orders ID after insert and remove: {order_ids}")
print(f"First two orders ID: {order_ids[0:2]}")

# Lab 8: Tuples — immutable product record
product = (501, "Notebook", 49.99)
id=product[0]
name=product[1]
price=product[2]
print(f"ID: {id}")
print(f"Name: {name}")
print(f"Price: {price}")
#product[2] = 12
print("Trying to change the price raise the error: 'TypeError: 'tuple' object does not support item assignment'. Tuples are inmutables")

# Lab 9: Sets — remove duplicate order IDs
order_ids = [201, 202, 201, 203, 202, 204]
unique_order_ids = set(order_ids)
print(f"Unique order IDs: {unique_order_ids}")
print(f"Count: {len(unique_order_ids)}")

# Lab 10: Dictionary — single customer record
customer = {"id": 1, "name": "Priya", "city": "Pune"}
customer["city"]="Mumbai"
print(f"Customer {customer["id"]} - {customer["name"]} lives in {customer["city"]}")

# Lab 11: Nested dictionaries — customers database
customers = {
    101: {"name": "Anil", "total_orders": 3},
    102: {"name": "Geeta", "total_orders": 5},
    103: {"name": "Sam", "total_orders": 1}
}
print(f"{customers[102]["name"]} has {customers[102]["total_orders"]} orders")

# Lab 12: Looping through dictionary items and aggregation
sales = {
    "Asha": 1200.50,
    "Rohan": 250.00,
    "Tina": 799.99
}
total_sales = 0
for v in sales.values():
    total_sales+=v
print(f"Total sales: {total_sales}")

# Lab 13: Find top customer by order amount using loops + dicts
totals = {"Asha": 1200.50, "Rajan": 3200.00, "Leela": 2450.75}
max_sales=0
customer_max_sale = []
for k, v in totals.items():
    if v > max_sales:
        max_sales = v
        customer_max_sale = k
    else:
        continue
print(f"Top customer {customer_max_sale} with {max_sales}")

# Lab 14: While loop simulating balance updates
balance = 500.0
transactions = [100.0, -50.0, 0.0, -600.0, 200.0]

ii = -1
while ii < len(transactions)-1:
    ii += 1
    transaction = transactions[ii]
    if transaction != 0:
        balance += transaction
        if balance < 0:
            print("Processing stopped early due to negative balance.")
            break
    else:
        continue
print(f"Final balance: {balance}")

# Same with a for
# for transaction in transactions:
#     if transaction == 0:
#         continue
#     else:
#         balance += transaction
#         if balance < 0:
#             break
    

# Lab 15: Choosing the right data structure — scenario tasks
product_ids = [701, 702, 703]
order_ids = [801, 802, 801, 803]
transactions = [10, -5, 10, 20]

inmutable_produtcs_id = tuple(product_ids)
unique_order_ids = set(order_ids)
print("Immutable product IDs:", inmutable_produtcs_id)
print("Unique order IDs for quick membership:", unique_order_ids)
print("Transactions list (order preserved, duplicates allowed):", transactions)

# Lab 16: Final Integrated Lab: Orders mini-ETL
orders = [
    {"order_id": 1, "customer": "Asha", "amount": 250.0, "product_id": 1001, "status": "delivered"},
    {"order_id": 2, "customer": "Ravi", "amount": 100.0, "product_id": 1002, "status": "pending"},
    {"order_id": 3, "customer": "Asha", "amount": 150.0, "product_id": 1003, "status": "delivered"},
    {"order_id": 4, "customer": "Meera", "amount": 400.0, "product_id": 1001, "status": "delivered"},
    {"order_id": 5, "customer": "Ravi", "amount": 50.0, "product_id": 1002, "status": "cancelled"}
]

# Filter orders with status "delivered". 
# Compute total amount per customer for delivered orders.
# Create a set of unique product_ids sold in delivered orders.

total_by_customers = {}
unique_product_ids = set({})
delivered_orders_count = 0

for order in orders:
    if order["status"] == "delivered":
        if order["customer"] not in total_by_customers.keys():
            total_by_customers[order["customer"]]=order["amount"]
        else:
            total_by_customers[order["customer"]]+=order["amount"]
        unique_product_ids.add(order["product_id"])
        delivered_orders_count +=1

# Produce a nested dictionary named report with:
# "totals_by_customer": {customer_name: total_amount}
# "unique_products": set(...)
# "delivered_count": count of delivered orders

report = {}
report["totals_by_customer"] = total_by_customers
report["unique_products"] = unique_product_ids
report["delivered_count"] = delivered_orders_count

print("Totals by customers:")
for k,v in report["totals_by_customer"].items():
    print(f"{k}: {v}")
print(f"Unique products sold (delivered): {report["unique_products"]}") 
print(f"Delivered order count: {report["delivered_count"]}")