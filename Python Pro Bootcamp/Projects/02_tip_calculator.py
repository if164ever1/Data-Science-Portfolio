print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? "))
tips = int(input("How much tips would you like to give? 10, 12, or 15 ? "))
number_of_people = int(input("How many people to spleat the bill? "))
tips_percent_convert = tips/100
paymant_amount = (total_bill + (total_bill * tips_percent_convert)) / number_of_people


print(f"Each person should pay: ${round(paymant_amount, 2)}")