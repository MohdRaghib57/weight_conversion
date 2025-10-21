# Converting weight from kg to lbs and vice versa


unit  = input("Please enter an unit: (kg/lbs)  ").strip()

mag = float(input("Enter the weight: "))

if unit == "kg":
    mag = mag * 2.205
    print(f"weight is: {round(mag , 3)} lbs")

elif unit == "lbs":
    mag = mag / 2.205
    print(f"weight is: {round(mag , 3)} kg")
else :
    print("Sorry! Entered unit is not valid for this program!")




