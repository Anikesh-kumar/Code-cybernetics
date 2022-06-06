# Write a Python program to convert temperatures to and from celsius, fahrenheit
temp = input("Enter temprature in format like (120F, 120C):")
degree = int(temp[:-1])
unit = temp[-1]
if unit.upper() == 'C' :
    result = int(round(( degree * 9/5) + 32))
elif unit.upper() == 'F' :
    result = int(round((degree - 32) * 5/9 ))
else :
    print("Enter Valid format of input")
    quit()
print("Temprature in", unit.upper(), "is", result,unit.upper())