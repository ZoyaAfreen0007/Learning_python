logged_in = True
Is_guest = False
Banned = True 
print  ((logged_in or Is_guest) and not Banned )

email= True
name = False
print (email or name)

#Check if a user's name is not empty and the age is greater than or equal to 18. 

username =  "Zoya" 
age = 22
print ((username != "" and username is not None) and age >=18)

# Check if the password is atleast 8 character long and doesnot contain spaces.

password = "12345678"
print(len(password) >= 8 and " " not in password ) 


#Check if a User's email is not empty, contains '@' and ends with '.com'.
email= "fhi@usf.com"
print(email is not None and email != "" and '@'in email and email.endswith (".com")  )

#Check if a username is string, not None and is longer than 5 character.
username = "Vandana"
print (isinstance(username,str) and username is not None and len(username) >= 5)

"""Check if a user is an admin or a moderator and either they are not banned or they have verified their email."""


is_user_admin = True
is_not_banned = True
email_verified = True
print(is_user_admin and is_not_banned and email_verified)


''' Validate the quality and correctness of email values:
1.must not be empty
2.must contain "." and "@".
3.must contain exactly 1 '@' symbol.
4.must end with ".com", ".org", ".net".
5.must not be longer than 254 characters.
6.must start and end with a letter or digit.'''



email = "Zoyaneerfa@gmail.com"
if email is not None and email !="":
       if email.endswith(".com") or email.endswith(".org") or email.endswith(".net") :
                if "." in email or "@" in email:
                    if len(email)< 254:    
                        if email.count("@")== 1 : 
                            if email[0].isalnum() and email[-1].isalnum(): 
                                 print("valid")
                        else:
                                 print ("Not")
else: 
    print ("sucker")              

'''Validate the quality and correctness of Passwords:
1.must not be empty.
2.must be atleast 8 characters.
3.must include at least 1 uppercase.
4.must include at least 1 lowercase.
5.must not be same as the email.
6.must not contain any spaces.
7.must start and end with a letter or digit'''

email = "Zoyaafreen0007@gmail.com"
password = "sulasula123"
password1 = password.lower()
password2 = password.upper()
'''print(password1)
print(password2)'''

if password == "":
    print("password cannot be empty.")
    
elif  (len(password))<8 :
    print ("password cannot be less than 8 characters")

elif password == password1 :
   print("password has no uppercase.")

elif password == password2:
   print("password has no lowercase.")

elif password == email:
    print ("password cannot be same as email")

elif " " in password :
    print ("Password must not contain any spaces.") 

elif not(password[0].isalnum () and password[-1].isalnum()):
    print ("password does not start or end with letter or digit.")

else: print("Valid")



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

emails=['zoyaafreen@gmail.com','zoyaneerfa@yahoo.com','baraa@outlook.de','suspicious entity','data@gmail.com']

for email in emails:
    if '.com' not in email and 'outlook.de' not in email:
        print ("unsafe data found", email)
        continue
    else:
        print (email)
    



#Check for missing names in a list.

names = ['ria','jia','pia','sia','mia','dia']
for name in names:
    if name == "zoya":
        print ("name found", name)
        break
else:
        print("name not found")




# Check whether any file name appears more than once.

file_list = ['report.csv','data.xlsx','summary.docx','report.csv','data.csv']
for file in file_list:
    if file_list.count(file) > 1:
        print ("duplicate found:", file)
        break

    else:
        print ("All files are unique.")    
