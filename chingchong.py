def display_toys(toys):
    print("Avalible toys!!")
    for toy,quantity in toys.items():
        print(f"{toy}:{quantity}")
def buy_toy(toys,toy,quantity):
    if toy in toys:
        if toys[toy] >= quantity:
            toys[toy] -= quantity
            print(f"you bought{quantity}{toy}:")
        else:
            print("you dunno have enough quantity to bought this...")
    else:
        print("Sorry we dunno have that thing if then go to another shop")
def main():
    toys = {'lazer gun':100,'samurai katana':150,'shuriken':50,'awm gun':90,'mp40':50}
    while True:
        print("\nWelcome to our shop")
        display_toys(toys)
        toy = input("Enter the thing you wanna buy(or type esc to quit:)").lower()
        if toy == 'exit':
            print("Thank you for supporting our sshhoopp...")
            break
        quantity = int(input("enter how many you wanna buy:"))
        buy_toy(toys,toy,quantity)
main()