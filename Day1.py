print(" Bitches don't die.")

print("Your Learning Path:\n\t-Python Basics\n\t-Data Engineering\n\t-AI")

print('''Your Learning Path:
\t-Python Basics
\t-Data Engineering
\t-AI''')

information = "info@datawithbaraa.com"
support = "support@datawithbaraa.com"
website = "www.datawithbaraa.com"
print ("The information of the Baraa platform can be collected from:", information )
print ("The support center of the Baraa platform can be connected through:", support )
print ("The website name of the Baraa platform is:", website )

age = 18
height = 181.45
name = "Britney Spears"
is_she_a_student = False
How_many_kids = None
print("My name is",name, ". I am ", age, "years old. My height is", height, "cm.")
print ("Am I a student:",is_she_a_student)
print ("How many kids do i have:",How_many_kids)

"+49 (176) 123-4567   ->     00491761234567  "

phone_no = "+49 (176) 123-4567"
print(phone_no.replace("+","00").replace(" ","").replace('(','').replace(')','').replace(" ","").replace("-",""))

'''
"968-Maria, ( D@t@ Engineer );; 27y  " ->   name: maria |  role: data engineer  | age: 27
'''

resume = "968-Maria, ( D@t@ Engineer );; 27y  "

resume1 = (resume.replace('"',"").replace('-'," ").replace(',',"").replace('(',"").replace('@',"a").replace('@',"a").replace(')',"").replace(';',"").replace('"',"").strip().lower()
)
print ("name:", resume1[4:9]," | ", "role:", resume1[11:24], " | ", "age:", resume1[26:] )


import math 
x= 1.89765
print (round (x))
print (math.floor (x))
print (math.ceil (x))
print (math.trunc (x))

import random
y = random.randint(1,100)
print(y)
if y % 2 == 0:
   print (y, "is an Even Number.")
else: 
    print (y, "is not an Even Number.")

