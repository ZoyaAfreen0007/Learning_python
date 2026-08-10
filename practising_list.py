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



