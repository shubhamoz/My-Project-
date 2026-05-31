while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 3:
        break

    a = float(input("First number: "))
    b = float(input("Second number: "))

    if choice == 1:
        print("Answer =", a + b)
    elif choice == 2:
        print("Answer =", a - b)
