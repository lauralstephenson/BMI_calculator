# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = float(weight) / float(height)**2
if (BMI < 18.5):
  print(f"Your BMI is {BMI}, you are underweight.")
elif (25 > BMI > 18.5):
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif (30 > BMI >= 25):
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif (35 > BMI >= 30):
  print(f"Your BMI is {BMI}, you are obese.")
else:
  print(f"Your BMI is {BMI}, you are clinically obese.")
  #or just bmi <25, bmi <30, bmi <35
