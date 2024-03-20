def display_toys(toys):
    print("!!Two toy gun for one watergun for free availible only on every saturday,sunday!!!")
    for toy,quantity in toys.items():
        print(f"{toy}:{quantity}")
def main():
    toys = {'toy gun':110,'watergun':100,'chess': 70,'card':20}
    while True:
      print("\n Welcome to the toy shop")
      display_toys(toys)
      toy = input("enter any toy you wanna buy(or type exit)to quit:").lower()
      if toy == "exit":
          print("Thanks for supporting our shop")
          break
      quantity = int(input("Enter how much you wanna buy:"))
main()
