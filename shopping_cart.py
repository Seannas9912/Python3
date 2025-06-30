#lesson 6 & 7
#create a shopping cart programme that will allow the user to add items to a cart, remove items, and view the cart contents.
#Have a exit option that will allow the user to exit the program.
#The program should also allow the user to view the total cost of the items in the cart.

foods = []
prices = []
total = 0

while True:
    food = input("Enter food item (or 'q' to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter price for {food}: R"))
        foods.append(food)
        prices.append(price)
        
print("\nYour shopping cart contains:")
for food in foods:
    print(food ,end=' ')
    
for price in prices:
    total += price
    
print(f"\nTotal cost: R{total}")
        