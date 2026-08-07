#find duplicates.

numbers = [10,20,30,40,20]  
numbers = [10,20,30,40,20]
for number in numbers:
    if numbers.count(number)>1:
        print ("duplicate found:", number)
        break
else:
        print("All numbers are unique.")   

numbers = [10, 20, 30, 40 ,20, 30, 50] #find duplicates.
numbers = [10, 20, 30, 40 ,20, 30, 50]
printed=[]
for number in numbers:
    if numbers.count(number)> 1:
        if number not in printed:
            print("duplicate found:", number)
        printed.append(number)
        
