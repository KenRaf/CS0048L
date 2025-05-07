import os
os.system('cls' if os.name =='nt' else 'clear')

def TemperatureConverter(x):
    while True:
        print("")
        print(" === Temperature Converter === \n")
        print("a. Convert Celsius to Fahrenheit")
        print("b. Convert Fahrenheit to Celsius")
        print("c. Exit to Main Menu")

        choice = input("Enter your operation (enter letter or operation): ")
        if choice in ['a' or 'Convert Celsius to Fahrenheit']:
            print(f"Converting {x} °C to Fahrenheit ")
            fahrenheit = (((9/5) * x) + 32)
            print(f"{x} °C to Fahrenheit is {fahrenheit}°F")

        elif choice in ['b' or 'Convert Celsius to Fahrenheit']:
            print(f"Converting {fahrenheit} °F to Celsius ")
            celsius = ((5/9) * (fahrenheit - 32))
            print(f"{fahrenheit} °C to Fahrenheit is {celsius:.2f}°C")

        elif choice in ['c' or 'Exit to Main Menu']:
            print("")
            print("Thank You for using Python Temperature Converter")
            print("Returning to Main Menu")
            break
        else:
            print("Invalid value for temperature! Please reenter a value: ")


while True:
    x = float(input("Enter temperature in °C: "))
    TemperatureConverter(x)
    choice = input("Do you want to try again? 1 for yes 0 for no: ")
    if choice == '1':
        continue
    else:
        print("Exiting Program")
        break
