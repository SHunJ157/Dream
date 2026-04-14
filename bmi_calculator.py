# BMI Calculator Tool
print("--- Welcome to the BMI Calculator ---")

weight = float(input("Enter your weight in kg: "))
height_cm = float(input("Enter your height in cm: "))

height_m = height_cm / 100
bmi = weight / (height_m ** 2)
bmi = round(bmi, 2)

print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print("Status: Underweight")
elif 18.5 <= bmi < 24:
    print("Status: Normal weight")
elif 24 <= bmi < 30:
    print("Status: Overweight")
else:
    print("Status: Obese")

