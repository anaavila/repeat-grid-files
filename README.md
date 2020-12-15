# repeat-grid-files
<strong>Program:</strong><br>
Populate Repeat Grids in Adobe XD

<strong>Description:</strong><br>
Simple program that reads a CSV file and creates files for each CSV column, and stores its data in a format ready to populate data Adobe XD’s repeat grids.

<strong>Goal:</strong><br>
The goal of this program is to help Adobe XD users spend less time creating files in the required format to populate text in repeat grids.

For designers, is convenient to collect data in spreadsheet files that is planned to populate their designs. It is also convenient that Adobe XD has a feature called repeat grids which allows designers to easily create repeated elements and drag files to populate text elements. What is not convenient is the process of creating text files that will contain data from the spreadsheet file in a required format. So at this point, designers have to manually create individual files to then populate its design. This program helps with that step by automatically creating each needed file in the desired format. 

<strong>How to use it:</strong>
- Make sure the first row of your spreadsheet contains names of column names.
  Those column names will be the names for each individual created text files.
- Export your spreadsheet file as CSV format.
- Open this program (populateXD.py) and type the CSV path name in ‘fileToRead’.
- Run the program and your files will be created and formatted ready to populate repeat grids on Adobe XD!

<strong>Note:</strong><br>
The spreadsheet file’s column names will be the names for each individual text files.<br>
Your files will be created in the folder where the populateXD.py is found.<br>

<h3>Try program with given file!</h3>
Download ```'populateXD.py'``` and ```'employees.csv'```.<br>
After you run the program, the following 4 files will be created:
<ul>
  <li>name.txt</li>
  <li>id.txt</li>
  <li>role.txt</li>
  <li>location.txt</li>
</ul>

Each file will look similar to the given 'name.txt' file.
