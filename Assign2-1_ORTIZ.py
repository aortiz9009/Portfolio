speed = int(input("\nEnter the speed of the vehicle in MPH:"))
while speed < 0:
    speed = int(input("Error: Enter a positive number:"))
    
hours = int(input("\nEnter the number of hours traveled: "))
while hours < 0:
        hours = int(input("Error: Enter a positive number: "))
        
distance = 0

output = "\nHour         Distance Traveled\n" \
         "--------------------------\n"
         
for hour in range(hours):
    distance = speed * (hour + 1)
    
    output += format(hour + 1) + "            " + \
              format(distance) + "\n"
              
print(output)
  