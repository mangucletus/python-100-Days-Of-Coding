#write a program that calculates the body mass index(BMI) from a user's weight and height
# The BMI is a measure of someone's weight taking into account their height
# 
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)
# BMI = W(kg)/H^2(m^2)  

a = input("enter your height in m : ")
b= input("enter your weight in kg : ")

h = float(a)
w = float(b)

bmi = round(w/pow(h, 2), 4)  # round off the bmi value to four decimal places 
results = str(bmi)  # convert float value to string to enable concatination
print("Your BMI value is: " + results +" kg/m^2" )


actual_bmi = int(bmi) # convert bmi to an integer value 
print(actual_bmi)