# BMI Calculator

# Ask the user for their height
height = input('Enter your height in inches: ')
# Ask the user for their weight
weight = input('Enter your weight in pounds: ')

# Calculate their BMI
BMI = (int(weight) / float(height) / float(height) * 703)
# Put BMI into whole number
intBMI = int(BMI)

# Tell user their BMI
print('Your BMI is ' + str(intBMI))