#In this program, we want to issue 'Provincial colours' award for participants who complete the three sports in 100 minutes or less. 
#We will issue the 'Provincial half colours'award to those who complete the sports in more than 100 minutes but less than or equal to 105 minutes.
#We will issue the 'Provincial Scroll' award for those who complete the sports in 106 minutes but less than or equal to 110 minunites.
#We will issue no award for a complete time above 110 minutes.
swimming_time = int(input("Enter swimming time (minutes): ")) 
cycling_time = int(input("Enter cycling time (minutes): "))
running_time = int(input("Enter running time (minutes): "))
total_time = (swimming_time + cycling_time + running_time)
if total_time <= 100:
 award = "Provincial Colours"
elif 101 <= total_time <= 105:
 award = "Provincial Half Colours"
elif 106 <= total_time <= 110:
  award = "Provincial Scroll"
else:
 award = "no award"

print ("Total time for the triathlon:", total_time)
print (award)
       

   
