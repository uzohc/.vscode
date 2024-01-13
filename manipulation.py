# Get user input
str_manip = input("Enter a string: ")
# 1) Calculate and display the length of str_manip
length_of_str = len(str_manip)
print("Length of str_manip:", length_of_str)
# 2) Find the last letter in str_manip
last_letter = str_manip[
-
1]
print("Last letter in str_manip:", last_letter)
# 3) Replace every occurrence of this letter with '@'
str_manip = str_manip.replace(last_letter, '@')
print("After replacing:", str_manip)
# 4) Print the last 3 characters in str_manip backwards
print("Last 3 characters backwards:", str_manip[-3:][::-1])
# 5) Create a five letter word
five_letter_word = str_manip[:3] + str_manip[-2:]
print("Five letter word:", five_letter_word)


