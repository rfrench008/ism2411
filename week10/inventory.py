# Excerise 1:build a list

print("--- Excersise 1: Build a List ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(len(inventory))

# Excersise 2: Index Practice

print("--- Excersise 2: Index Practice ---")
print(inventory[0])
print(inventory[-1])

middle = len(inventory) //2
print(inventory[middle])

# Excerise 3

print("--- Excerise 3: List Slicing ---")

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# --- Excerise 4: List Methods ---

print("--- Excerise 4: List Methods ---")

inventory.append("envelope")
inventory.append("tape")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

print("--- Excerise 5: Tuple Comparison ---")
coords = (40.7128,-74.0060)

try:
    coords[0]= 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident")

print("--- Excerise 6: List Average Sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total/count
print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

best = sales [0]
worst = sales [0]

for amount in sales:
    if amount> best:
        best = amount
    if amount < worst:
        worst = amount

print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")

print("--- Excerise 7: Accmulator patetrn ---")

prices = [9,99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))

print(prices)
print(discounted)

print("--- Excerise 8: Filter ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales)/ len(high_sales):.2f}")


# Reflection

# Q.1
# I was suprised at how strings and interges could both be used togther and you don't need two seprate list.
# It makes it so that now you can be more organized with the woek and how it's presented.


# Q.2
# Having a list of names of people with money owed for the money borrowed. Doing it in python will save
# an abudance amount of time when it comes to retrieving information.