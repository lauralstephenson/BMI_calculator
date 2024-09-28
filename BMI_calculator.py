# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
BMI = float(weight) / float(height)**2
print(int(BMI))

#OR 
#weight_as_int = int(weight)
#height_as_float = float(height)
#Using the exponent operator **
#bmi = weight_as_int / height_as_float**2

#OR using multiplication and PEMDAS
#bmi = weight_as_int / (height_as_float * height_as_float)