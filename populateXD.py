############################################
#
# @Program: populateXD.py
# Creates files to populate repeat grids in Adobe XD
#
# @Author Ana Avila (github.com/anaavila)
#
# @Date September 2020
#
# @Description
# Simple program that reads a CSV file, creates files
# for each CSV column, and stores its data in a format ready 
# to populate data for Adobe XD's repeat grids.
#
############################################


import csv

# MODIFY: store the name or path of the CSV. (save and build program)
fileToRead = "employees.csv"

# opening and reading a CSV file
f = open(fileToRead, 'r')
print("Opening " + fileToRead)
reader = csv.reader(f)
allData = list(reader)
f.close()
print("Closing " + fileToRead)

# storing column names for file names
file_names = []
for col_item in allData[0]:
	file_names.append(col_item.lower()+".txt")

# creating, opening, and populating files (named as column names)
rows = allData[1:]
for col in range(len(file_names)):
	working_file = open(file_names[col], 'w')
	print("Creating and opening " + str(file_names[col]))
	temp_data = []
	for row in range(len(rows)):
		temp_data.append(rows[row][col])
	working_file.write('\n'.join(temp_data))
	print("Writing data to " + str(file_names[col]))
	working_file.close()
	print("Closing " + str(file_names[col]))

print("A total of " + str(len(file_names)) + " files were created.")
print("Your data is ready to populate repeat grids on Adobe XD!")