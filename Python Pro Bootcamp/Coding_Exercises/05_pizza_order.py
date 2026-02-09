
small_pizza = 's'
medium_pizza = 'm'
large_pizza = 'l'

print("Welcome to Python Pizza Deliviries!")
size = input("What size of pizza do you want? S, M, or L: ").strip().lower()
pepperoni = input("Do you want pepperony on your pizza ? Y or N: ").strip().lower()
extra_cheese = input("Do you want extra cheese on your pizza ? Y or N: ").strip().lower()

small_pizza_prise = 15
medium_pizza_prise = 20
large_pizza_prise = 25

# Extra
pepperoni_yes_on_small_pizza = 2
pepperoni_yes_on_medium_large_pizza = 3
cheese_yes_on_any_pizza = 1

bill = 0

if size == small_pizza:
    bill += small_pizza_prise
    if pepperoni == 'y':
        bill += pepperoni_yes_on_small_pizza
    if extra_cheese == 'y':
        bill += cheese_yes_on_any_pizza
elif size == medium_pizza:
    bill += medium_pizza_prise
    if pepperoni == 'y':
        bill += pepperoni_yes_on_medium_large_pizza
    if extra_cheese == 'y':
        bill += cheese_yes_on_any_pizza
elif size == large_pizza:
    bill += large_pizza_prise
    if pepperoni == 'y':
        bill += pepperoni_yes_on_medium_large_pizza
    if extra_cheese == 'y':
        bill += cheese_yes_on_any_pizza

print(f"Your final bill is ${bill}")
