#tip calculator to determine the amount each person should pay 


print("Welcome to the tip calculator.\n ")
total_bill = float(input("What was the bill? :\n "))

pay_tip = float( input("What percentage tip would you like to give? 10, 12 or 15?\n "))

pay_percentage = pay_tip/100

percentage_value = pay_percentage * total_bill
final_bill = total_bill + percentage_value
num_people = int(input("How many people to slip the bill? :\n "))


each_person_pay = round((final_bill/num_people), 2)
print(f"Each person should pay: ${each_person_pay}\n ")


