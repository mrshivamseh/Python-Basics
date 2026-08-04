from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius

temperature = float(input("Enter temperature:"))
unit = input("Enter unit(C/F):")

if unit == "C":
    result = celsius_to_fahrenheit(temperature)
    print("Fahrenheit:",result)

elif unit == "F":
    result = fahrenheit_to_celsius(temperature)
    print("Celsius:",result)

else:
    print("Invalid unit")