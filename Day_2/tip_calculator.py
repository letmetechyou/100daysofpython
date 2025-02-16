#This project takes the amount of the bill and determines how much each person has to pay based on the amount of tip given



print("Welcome to the tip Calculator!\n")
bill = float(input("What was the total Bill: "))
total_tip = int(input("How much of a tip would you like to give? 10, 12 or 15: "))
total_people = int(input("How many people to split the bill: "))
tip_percent = total_tip / 100
total_tip_amount = bill * tip_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / total_people
finall_amount = round(bill_per_person, 2)
print(f"Each person should pay {finall_amount} dollars")