def display_fruits(fruits):
    print("!! Available fruits:")
    for fruit,quantity in fruits.items():
        print(f"{fruit}:{quantity}")

def buy_fruit(fruits, fruit, quantity):
    if fruit in fruits:
        if fruits[fruit] >= quantity:
            fruits[fruit] -= quantity
            print(f"ÿou bought {quantity} {fruit}.")
        else:
            print("sorry, we don't have enough quantity of that fruit.")
    else:
        print("Sorry, we don't have that fruit.")

def add_fruits(fruits,fruit,quantity):
    if fruit in fruits:
        fruits[fruit] += quantity
    else:
        fruits[fruit] = quantity
def main():
    fruits = {'apple':50, 'banana':15, 'mango':40, 'watermelon':35}

    while True:
        print("\n Welcome to the fruit shop!")
        display_fruits(fruits)

        fruit = input("Ënter the fruit you want to buy (or type 'exit' to quit):").lower()

        if fruit == 'exit':
            print("Thanks for shopping with us!")
            break
        
        quantity = int(input('Enter the quantity'))

        buy_fruit(fruits, fruit, quantity)
    
    new_fruit = input("what new fruits to add").lower()
    quantity_purchased = int(input("what the quantity that purchased"))
    add_fruits(fruits, new_fruit, quantity_purchased)
main()