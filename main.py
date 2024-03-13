def display_fruits(fruits):
    print("!! Available fruits:")
    for fruit,quantity in fruits.items():
        print(f"{fruit}:{quantity}")
def main():
    fruits = {'Ápple':50, 'banana':15, 'mango':40, 'watermelon':35}

    while True:
        print("\n Welcome to the fruit shop!")
        display_fruits(fruits)

        fruit = input("Ënter the fruit you want to buy (or type 'exit' to quit):").lower()

        if fruit == 'exit':
            print("Thanks for shopping with us!")
            break
        
        quantity = int(input('Enter the quantity'))


main()