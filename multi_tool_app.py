def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def square(num):
    return num * num

def power(a, b):
    return a ** b


while True:
    print("=" * 30)
    print("1. Calculator")
    print("2. Number Analyser")
    print("3. Exit")
    print("=" * 30)

    main_choice = int(input("Enter Choice: "))

    if main_choice == 3:
        break

    elif main_choice == 1:
        while True:
            print("-" * 30)
            print("--- CALCULATOR ---")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Square")
            print("6. Power")
            print("7. Back")
            print("-" * 30)

            choice = int(input("Enter Choice: "))

            if choice == 7:
                break

            elif choice == 1:
                num1 = float(input("Enter First Number: "))
                num2 = float(input("Enter Second Number: "))
                print("Result:", add(num1, num2))

            elif choice == 2:
                num1 = float(input("Enter First Number: "))
                num2 = float(input("Enter Second Number: "))
                print("Result:", subtract(num1, num2))

            elif choice == 3:
                num1 = float(input("Enter First Number: "))
                num2 = float(input("Enter Second Number: "))
                print("Result:", multiply(num1, num2))

            elif choice == 4:
                num1 = float(input("Enter First Number: "))
                num2 = float(input("Enter Second Number: "))
                if num2 == 0:
                    print("Cannot divide by zero")
                else:
                    print("Result:", divide(num1, num2))

            elif choice == 5:
                num = float(input("Enter Number: "))
                print("Result:", square(num))

            elif choice == 6:
                num1 = float(input("Enter First Number: "))
                num2 = float(input("Enter Second Number: "))
                print("Result:", power(num1, num2))

            else:
                print("Invalid Choice")

    elif main_choice == 2:
        while True:
            print("-" * 30)
            print("--- NUMBER ANALYSER ---")
            print("1. Even / Odd")
            print("2. Prime Check")
            print("3. Palindrome Check")
            print("4. Armstrong Check")
            print("5. Factorial")
            print("6. Digit Sum")
            print("7. Largest Digit")
            print("8. Smallest Digit")
            print("9. Back")
            print("-" * 30)

            choice = int(input("Enter Choice: "))

            if choice == 9:
                break

            elif choice == 1:
                num = int(input("Enter your number: "))
                if num % 2 == 0:
                    print("Even Number")
                else:
                    print("Odd Number")

            elif choice == 2:
                num = int(input("Enter your number: "))
                is_prime = True
                if num < 2:
                    is_prime = False
                else:
                    for i in range(2, num):
                        if num % i == 0:
                            is_prime = False
                            break
                if is_prime:
                    print("Prime Number")
                else:
                    print("Not Prime Number")

            elif choice == 3:
                num = int(input("Enter your number: "))
                original = num
                rev = 0
                temp = num
                while temp > 0:
                    digit = temp % 10
                    rev = rev * 10 + digit
                    temp = temp // 10
                print("Reverse:", rev)
                if rev == original:
                    print("Palindrome")
                else:
                    print("Not Palindrome")

            elif choice == 4:
                num = int(input("Enter your number: "))
                original = num
                total = 0
                temp = num
                while temp > 0:
                    digit = temp % 10
                    total += digit ** 3
                    temp = temp // 10
                if total == original:
                    print("Armstrong Number")
                else:
                    print("Not Armstrong Number")

            elif choice == 5:
                num = int(input("Enter your number: "))
                factorial = 1
                if num < 0:
                    print("Factorial not possible for negative numbers")
                else:
                    for i in range(1, num + 1):
                        factorial *= i
                    print("Factorial:", factorial)

            elif choice == 6:
                num = int(input("Enter your number: "))
                digit_sum = 0
                temp = num
                while temp > 0:
                    digit = temp % 10
                    digit_sum += digit
                    temp = temp // 10
                print("Digit Sum:", digit_sum)

            elif choice == 7:
                num = int(input("Enter your number: "))
                largest = 0
                temp = num
                while temp > 0:
                    digit = temp % 10
                    if digit > largest:
                        largest = digit
                    temp = temp // 10
                print("Largest Digit:", largest)

            elif choice == 8:
                num = int(input("Enter your number: "))
                smallest = 9
                temp = num
                while temp > 0:
                    digit = temp % 10
                    if digit < smallest:
                        smallest = digit
                    temp = temp // 10
                print("Smallest Digit:", smallest)

            else:
                print("Invalid Choice")

    else:
        print("Invalid Choice")
