#  STUDENT MARKS ANALYSIS USING LISTS FUNCTIONS IN PYTHON.      


marks = [78, 65, 89, 92, 56, 74, 81, 45, 95, 67]

print("Marks:", marks)

# Total marks
total = sum(marks)

# Average marks
average = total / len(marks)

# Highest and lowest marks
highest = max(marks)
lowest = min(marks)

# Students who scored 75 or more
above_75 = [mark for mark in marks if mark >= 75]

# Students who failed
failed = [mark for mark in marks if mark < 40]

print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Marks >= 75:", above_75)
print("Failed marks:", failed)
    

''' Store only True states. Create a list containing only the states when the state is True.
Given: items = ["a","toggle","b","c", "toggle","e" ]
'''

state = True
result = []
items = ["a","toggle","b","c", "toggle","e" ]
for item in items:
   if item == "toggle":
      state = not state
   if state == True:
      result.append(state)
  
      print(result)


#. Two possible trigger words. Toggle the state whenever on or off appears.abs
#. Condition: both "on" and "off" should toggle the state.

state = True
result= []

items = ["hello", "on", "abc", "off", "xyz", "on", "test"]

for item in items:
    if item == "on" or "off":
        state = not state
        result.append(state)
    else:
        result.append(state)
print(result)         


#. ADD COUNTING:-
#. final state= .....abs
#. Number of changes = ....abs

state = True
result = []

items = ["x", "change", "y","change", "z","change"]
for item in items:
    if item == "change":
        state = not state
        result.append(state)
    else:
         result.append(state)
print (result)
 
list = 0
for item in items:
    if item == "change":
        list += 1
    else:
        list += 0

print (list)




















