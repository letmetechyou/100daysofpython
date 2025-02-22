#this code will determine the amount it will cost to deliver pizza based on toppings and pizza size

print("Welcome to the pizza delivery app")
order_status = input("Would you like to order pizza? Y or N: ")
bill = 0 
#todo: work out how much they need to pay based on size of pizza
#todo: work out how much to add to their bill based on if they want pepperoni
#todo: work out the final amount based on if thye want extra cheese
if order_status.lower() == "y":
    size = input("What size pizza would you like? S, M , L: ")
    if size.lower() == "s":
        bill = 10
    elif size.lower() == "m":
        bill = 15
    elif size.lower() == "l":
        bill = 20
    else:
        print("Invalid size")
    add_pepperoni = input("Do you want pepperoni? Y or N: ")
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if add_pepperoni.lower() == "y":
        if size.lower() == "s":
            bill += 2
        else:
            bill += 3
    if extra_cheese.lower() == "y":
        if size.lower() == "s":
            bill += 2
        else:
            bill += 3
    print(f"Your final payment is {bill}")
else:
    print("Thanks for stopping by")

