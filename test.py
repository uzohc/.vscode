
# Function to print the asterisk '*` patterns in double incrmental order.
def print_asterisk_triangle(rows):
    for i in range(1, rows + 1):
# Print spaces before the asterisks
        for j in range(rows - i):
            print(" ", end="")
        
        # Print asterisks
        for k in range(2 * i - 1):
            print("*", end="")
        
        # Move to the next line after each row
        print()

# Specify the number of rows for the triangle
num_rows = 5

# Call the function to print the pattern
print_asterisk_triangle(num_rows)

#output 
    *
   ***
  *****
 *******
*********
