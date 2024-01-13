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

       

   
