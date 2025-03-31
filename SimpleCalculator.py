def main():
   def addition():  # addition function
    a=int(input("Please insert first number: "))
    b=int(input("Please insert secound number: "))
    print("The sum of the numbers is: "+ str(a + b)+ ".")
   def substraction(): #substraction function
    a=int(input("Please insert first number: "))
    b=int(input("Please insert secound number: "))
    print("The difference of the numbers is: "+ str(a - b)+ ".")
   def multiply():  #multiplication function
    a=int(input("Please insert first number: "))
    b=int(input("Please insert secound number: "))
    print("The product of the numbers is: "+ str(a * b) + ".")
   def division(): #division function
    a=int(input("Please insert first number: "))
    b=int(input("Please insert secound number: "))
    if b > 0:
        print("The quotient of the numbers is: " + str(a / b) + ".")
    else:
        print("Error: Division by zero is not allowed.")
    


   while True:
    print("Select operation:") # asking for input
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("Press Enter to exit.")
  
    answear=input("->")
    if answear == "":  # enter=>exit
            break  

    if answear in ("1", "2", "3", "4"):  
        answear = int(answear)  
        if answear == 1:
            addition()
        if answear == 2:
            subtraction()
        if answear == 3:
            multiply()
        if answear == 4:
            division()
    else:
       print("Invalid choice. Please choose a number from 1 to 4.")



if __name__ == '__main__':
    main()
    