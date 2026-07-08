import numpy as np

# Lab 1: Simple Greeting Function
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")

# Lab 2: Add Two Numbers
def add_numbers(a, b):
    return a+b
result = add_numbers(15,27)
print(result)

# Lab 3: BMI Calculator (Function with Return)
def calculate_bmi(weight_kg, height_m):
    return round(weight_kg / (height_m ** 2),2)
print(calculate_bmi(70,1.75))

# Lab 4: Billing Calculator with Default Arguments
def calculate_total(amount, tax_rate=0.05):
    subtotal= amount
    tax= subtotal*tax_rate
    total=subtotal+tax
    return total
print(f"Total: {calculate_total(100):.2f}")
print(f"Total: {calculate_total(200, 0.12):.2f}")

# Lab 5: Function Naming and Docstring — Discount Calculator
def apply_discount(price, discount_percent):
    """Calculate the price discounted."""
    price_discounted = price*(1-discount_percent/100) 
    return price_discounted
print(apply_discount(250, 10))

# Lab 6: Reusable Utility — Normalize Names
def normalize_name(name):
    clean_name=name.strip().replace("  "," ").title()
    return clean_name
print(normalize_name("  alice   johnson "))
print(normalize_name("BOB mcDONALD"))

# Lab 7: Function Returning Multiple Values — Basic Stats
def basic_stats(numbers):
    count = len(numbers)
    total = sum(numbers)
    mean = total/count if len(numbers)>0 else None
    return count, total, mean
count, total, mean = basic_stats([10,20,30])
print(f"Count: {count}")
print(f"Total: {total}")
print(f"Mean: {mean}")

# Lab 8: Apply Function to a List of Amounts — apply_tax
def apply_tax(amounts, tax_rate=0.1):
    taxed_amounts=[]
    for amount in amounts:
        tax= amount*tax_rate
        total = amount-tax
        taxed_amounts.append(total)
    return taxed_amounts
amounts = [100, 200, 350]
print(apply_tax(amounts, tax_rate=0.05))

# Lab 9: Function with Optional Argument and Simple Validation
def process_score(score, max_score=100):
    # percentage_score = None if score > max_score | score < 0 else score/max_score*100 # other if structure
    percentage_score = score/max_score*100 if score in range(0,101) else None
    return percentage_score
print(process_score(85))
print(process_score(150))

# Lab 10: NumPy — Create Arrays
py_list = [10, 20, 30, 40, 50]
arr = np.array(py_list)
print(arr)
print(arr.dtype)

# Lab 11: Array Indexing and Slicing
arr = np.array([10, 20, 30, 40, 50])
print(f"First: {arr[0]}")
print(f"Last: {arr[-1]}")
print(f"Slice 1:4 -> {arr[1:4]}")

# Lab 12: Array Filtering (Boolean Masks)
sales = np.array([120, 250, 90, 400, 60])
high_sales = sales[sales > 100]
print(high_sales)

# Lab 13: Vectorized Array Operations
prices = np.array([100.0, 200.0, 300.0])
taxed = prices*1.05
print(f"First: {taxed}")
discounted = prices - (prices * 0.1)
print(f"Discounted: {discounted}")

# Lab 14: NumPy Aggregations — sum, min, max, mean
data = np.array([10, 20, 30, 40, 50])
total=np.sum(data) # or data.sum()
minimun=np.min(data) # or data.min()
maximum=np.max(data) # or data.max()
mean=np.mean(data) # or data.mean()
print(f"Total: {total}")
print(f"Minimum: {minimun}")
print(f"Maximum: {maximum}")
print(f"Mean: {mean}")

# Lab 15: Final Integrated Lab — Sales ETL with Functions + NumPy
def clean_sales(arr):
    sales = np.array(arr, dtype=float)
    sales[sales <= 0] = np.nan
    cleaned_sales = sales[~np.isnan(sales)]
    return cleaned_sales

def apply_discount_to_large_sales(arr, threshold=200, discount_rate=0.1):
    discouted_sales = arr.copy()
    mask = discouted_sales > threshold
    discouted_sales[mask] = discouted_sales[mask]*(1-discount_rate)
    return discouted_sales

def summarize_sales(arr):
    summary = {}
    sales = np.array(arr).copy()
    summary["total"]= sales.sum()
    summary["count"] = np.size(sales)
    summary["mean"] = round(sales.mean(),2)
    summary["maximum"] = sales.max()
    summary["minimum"] = sales.min()
    return summary
raw_sales = [120.0, 250.5, np.nan, -20.0, 400.0, 150.0, 0.0, 300.0]
cleaned_sales = clean_sales(raw_sales)
#print(cleaned_sales)
discounted_sales = apply_discount_to_large_sales(cleaned_sales)
#print(discounted_sales)
summary = summarize_sales(discounted_sales)
print(f"Total: {summary["total"]:.2f}")
print(f"Count: {summary["count"]}")
print(f"Mean: {summary["mean"]:.2f}")
print(f"Maximum: {summary["maximum"]}")
print(f"Mnimum: {summary["minimum"]}")
