# Q7.Write function bmi that calculates body mass index (bmi = weight / height2).


def index(bmi):
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    elif bmi > 30:
        return "Obese"
    else:
        pass
print(index(20))
        
        
        
