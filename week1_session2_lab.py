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

