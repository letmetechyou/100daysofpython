print("Welcome to the rollercoaster!")
print( 10 % 3)
height = int(input("What is your height in cm? "))
bill = 0
if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("child tickets are $5")
    elif age <= 18:
        bill = 7
        print("youth tickets are $7.")
    else:
        bill = 12
        print("adult tickets are 12")
    wants_photo = input("Do you want a photo taken? Type y or n ")
    if wants_photo == "y":
        #add $3 to their bill
        bill += 3
    
    print(f"Your final bill is {bill}")

else:
    print("Sorry you have to grow taller before you can ride")