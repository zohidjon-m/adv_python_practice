# Assignment 2: c_to_f and f_to_c with a simple menu-driven main()

def c_to_f(c):
    return (9.0 / 5.0) * c + 32.0

def f_to_c(f):
    return (5.0 / 9.0) * (f - 32.0)

def main():
    print("Temperature Converter")
    print("1) C -> F")
    print("2) F -> C")
    choice = input("Choose 1 or 2: ").strip()

    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c} °C = {c_to_f(c)} °F")
    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f} °F = {f_to_c(f)} °C")
    else:
        print("Invalid choice. Please run again and choose 1 or 2.")


main()