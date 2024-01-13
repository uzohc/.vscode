def main():
    numbers = []

    while True:
        user_input = input("Enter a number (or -1 to stop): ")

        # Check if the user wants to exit
        if user_input == "-1":
            break

        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if numbers:
        average = sum(numbers) / len(numbers)
        print(f"Average of the entered numbers (excluding -1): {average}")
    else:
        print("No numbers entered.")

if __name__ == "__main__":
    main()