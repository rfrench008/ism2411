# --- Excerise 1 ----

# Defining a function
def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2= calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# --- Excerise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
       return price * 0.85 
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function with different tiers

original_price = 2000

for tier in [ "gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# --- Excerise 3 ---

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

#Calling the final_price function
print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# --- Excerise 4 ---

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate= 0.07
for price, tier in orders: 
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

# --- Excerise 5 ---

# Issue 1. total was = to the sale. I couldn't find this one but the AI explained that the since it was formated that way the toatl was always looping. 
# Issue 2. I was missing the colon, I found this one and the AI did match what I found.
# Issue 3. I was using <= instead of <. Now it stops the loop before the i reaches 5


# --- Excerise 6 ---

x = 100 # global x 

def double_it():
    x= 999 # local x 
    return x * 2

print(x)
print(double_it())
print(x)