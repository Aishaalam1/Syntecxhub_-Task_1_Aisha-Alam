def add(a,b): 
    return a+b 
def subtract(a,b): 
    return a-b 
def multiply(a,b): 
    return a*b 
def divide(a,b): 
    if b==0: 
        return "can't divide"
    return a/b 

def show_menu():
    print("\n____Menu Driven Calculator____")
    print("1. Perform Addition")
    print("2. Perform Subtraction")
    print("3. Perform Division")
    print("4. Perform Multiplication")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = divide(num1, num2)
        elif choice == '4':
            result = multiply(num1, num2)
        else:
            print("Invalid choice! Please select between 1-5.")
            continue
        print("Result:", result)

if __name__=="__main__":
    main()
