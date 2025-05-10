print("Welcome to the tip calculator!")
bill_cost = float(input("What was the total bill? $"))



percent10 = 10
percent12 = 12
percent15 = 15
percent20 = 20
percent10tip = float(bill_cost / 10)
percent12tip = float(bill_cost * .12)
percent15tip = float(bill_cost * .15)
percent20tip = float(bill_cost * .20)

#tip_options = int(10 12 15 20)

print(input(f"How much tip would you like to give? 10 12 15 20"))
print("Person, your bill comes to a whopping:")
if percent10:
    print(round(bill_cost + percent10tip, 2))
elif percent12:
    print( str("$"), str(round(bill_cost + percent12tip, 2)), str("better slow down on those carbs!"))
elif percent15:
    print(round(bill_cost + percent15tip, 2))
elif percent20:
    print(round(bill_cost + percent20tip, 2))
else:
    print("please choose a tip amount listed :)")



