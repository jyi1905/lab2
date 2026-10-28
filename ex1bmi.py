def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi= weight/(height*height)
    print(f"{bmi}")
    if bmi <18.5:
        print("classification = underweight")
    elif bmi>=18.5 and bmi<= 25.0:
        print("classification = normal weight")
    else:
        print("classification = overweight")

calculate_bmi(weight=57, height=1.73)




