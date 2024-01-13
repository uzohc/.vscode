pattern = "*"
# Create the pattern
lines = 10
turn_point = lines/2
for num in range (1, lines):
    to_print = pattern*num
#Create the reverse pattern
    if num>=turn_point:
        count_down = lines - num
        to_print = pattern*count_down
    
    print(to_print)