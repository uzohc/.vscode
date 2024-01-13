print("Welcome to the error program")
print("\n")

# Variables declaring the user's age, casting the str to an int, and printing the result
age_str = "24 years old"
age = int(age_str[:2])  # Extracting the numeric part and converting to int
print("I'm " + str(age) + " years old.")

# Variables declaring additional years and printing the total years of age
years_from_now = 3  # Removing the quotes to treat it as an integer
total_years = age + years_from_now

print("The total number of years: " + str(total_years))

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")

#Changes made:

#1.print statements should use parentheses in Python 3.
#2.Corrected the variable assignment for age_str and extracted the numeric part using slicing.
#3.Removed extra = in age_str.
#4.Converted age to a string when concatenating it with the print statement.
#5.Removed quotes around the years_from_now value to treat it as an integer.
#6.Used the correct variable name total_years when printing the total number of years.
#7.Corrected the variable name total to total_years when calculating total_months.
#8.Converted total_months to a string when concatenating it with the print statement.




