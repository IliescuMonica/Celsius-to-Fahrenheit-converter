def main():
    def convert():
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 1.8) + 32   #converting Celsius to Fahrenheit
        print(str(c) + " Celsius is equal to " + str(f)+" Fahrenheit")

    convert()
    again = input("Do you want to convert another temperature? (yes/no): ")
    while again in ("yes","y"):
        convert()
        again = input("Do you want to convert another temperature? (yes/no): ")
    input("Press Enter to exit...")

    

if __name__ == "__main__":
    main()