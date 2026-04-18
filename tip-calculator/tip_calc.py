print("Welcome to the bill tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
bill_percent= tip/100
bill_plus_tip=bill_percent * bill + bill
people=int(input("How many people to split the bill?"))
final_bill=bill_plus_tip/people
print(f"Each person should apy: ${final_bill}")
