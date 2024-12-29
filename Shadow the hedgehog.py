h = float(input("Enter height in m"))
w = float(input("Enter weight in kgs"))
BMI = w / (h**2)
if BMI <= 18.4:
    print("You are under weight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("you are over weight")
elif BMI <= 34.9:
    print("You are obese")
else: 
    print("go to Dr robotnick")