#LOOPS:- ('FOR' LOOP )

tables=[1,2,3,4,5,6,7,8,9,10]
x = 7
for table in tables:
    x = x * table
    print (x)

x = 7
for i in range (1, 11):
    y = x * i
    print("7 *", i, "=" , y)
x = "*"
for i in range (1,7):
    y = x * i
    print (y)

# loop through a list of days and print only the working days,skipping the weekends.


days=["sun","mon","tue", "wed", "thurs", "fri", "sat"]  
for day in days:
    if day == "sun":
        continue
        print(day)
    elif day == "sat":
        break    
    print (day)

    #scan emails to block unsafe data entering your system.


