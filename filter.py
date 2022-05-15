ages = [16, 23, 18, 45, 81]

def myFunc(ages):
    if ages < 18:
        return False
    else: 
        return True

adults = filter(myFunc, ages)

for x in adults:
    print(x)
