# Basal Metabolic Rate Calculator

weight=int(input("Enter Your Weight in KG: \n"))
height=int(input("Enter Your Height in CM: \n"))
age=int(input("Enter Your Age in years: \n"))
isMale= str(input("Are You Male? (y/n)"))

if isMale == "y":
    isMale = True
elif isMale == "n":
    isMale = False
else:
    print("Error")
    quit()

if isMale:
          # Miffin St.Jeor Eqution for males

    bmr=66.5+(13.75*weight)+(5*height)-(6.755*age)
else:
          # Miffin St.Jeor Eqution for females

    bmr=655.1 + (9.6 * weight) +(1.8 * height) -(4.7*age)


bmr=round(bmr)
print(bmr)