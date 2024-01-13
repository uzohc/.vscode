#A buggy code was given, I had to bug the code. The steps taken to debug it were outlined below.
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16
full_spec = "This is a {0}. It is a {1} and it has {2} teeth".format(animal, animal_type, number_of_teeth)
print(full_spec)

#STEPS TAKEN TO DEBUG
# 1. The variable Lion should be a string, so it needs to be enclosed in quotes.
# 2. The print statement is not correctly formatted. In Python 3, it should use parentheses.
# 3, In this corrected version, I've enclosed the value of the animal variable in double quotes
# to make it a string. Additionally, I used the format method to insert the values of the variables 
# into the string, and I fixed the print statement by adding parentheses.
