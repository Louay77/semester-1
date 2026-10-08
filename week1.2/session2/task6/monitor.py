# Week 1.2, Session 2: Task 6
temp = int(input("enter temperature in celsius:"))
pressure = int(input("enter pressure is PSI :"))
Status = int(input("enter operational status: "))
if temp > 80 :
    print(" temperature too high")
elif temp < 80 and temp > 50 :
    print (" temperature is within safe limits")
else:
    print(" temperature is low, no action needed")

if pressure > 100:
    print ("pressure is high, maintenance need")
elif pressure < 100 and pressure > 70 :
    print ("pressure is stable")
else:
    print("presure is low, everything is operating normally")

if Status == 1:
    if pressure > 100 or temp > 80:
        print ("machine is running in unsafe conditions, shut it down")
    else:
        print ("machine is running normally")
if Status == 0:
    print("machine is stopped, no action needed")


