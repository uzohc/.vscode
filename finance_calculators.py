print ("import math")
def calculate_investment():
    try:
        principal = float(input("Enter the principal amount: "))
        interest_rate = float(input("Enter the interest rate (as a percentage): "))
        time = int(input("Enter the number of years: "))
        interest_type = input("Enter 'simple' or 'compound' interest: ").lower()
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")
        return

    # Convert interest rate to decimal
    interest_rate /= 100

    if interest_type == 'simple':
        # Simple interest formula
        interest = principal * interest_rate * time
        total_amount = principal + interest
    elif interest_type == 'compound':
        # Compound interest formula
        total_amount = principal * (1 + interest_rate) ** time
        interest = total_amount - principal
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")
        return

    print(f"\nThe interest earned is: ${interest:.2f}")
    print(f"The total amount after {time} years is: ${total_amount:.2f}")


def calculate_bond_payment():
    try:
        present_value = float(input("Enter the present value of the house: "))
        interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
        months = int(input("Enter the number of months to repay the bond: "))
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")
        return

    # Convert interest rate to monthly and calculate bond payment
    monthly_interest_rate = interest_rate / 12 / 100
    bond_payment = present_value * (monthly_interest_rate * (1 + monthly_interest_rate) ** months) / \
                   ((1 + monthly_interest_rate) ** months - 1)

    print(f"\nThe monthly bond payment is: ${bond_payment:.2f}")


def main():
    print("Welcome to the Financial Calculator!")
    print("Choose an option:")
    print("1. Investment - to calculate the amount of interest you'll earn on your investment.")
    print("2. Bond - to calculate the amount you'll have to pay on a home loan.")

    user_choice = input("Enter 'investment' or 'bond' to proceed: ").lower()

    if user_choice == 'investment':
        calculate_investment()
    elif user_choice == 'bond':
        calculate_bond_payment()
    else:
        print("Invalid input. Please enter 'investment' or 'bond'.")

if __name__ == "__main__":
    main()

