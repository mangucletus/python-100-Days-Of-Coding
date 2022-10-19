#Your life in weeks
# create a program using maths and f-strings that tells us how many days, weeks, months we have left if we live until 90 years old.


getAge = input("What is your current age: ")
age = int(getAge)

yearsRemainig = 90 -age
daysRemaining = yearsRemainig * 365
weeksRemaining = yearsRemainig * 52
monthsRemaining = yearsRemainig * 12

print(f"You have {daysRemaining} days, {weeksRemaining} weeks, and {monthsRemaining} months left.")
