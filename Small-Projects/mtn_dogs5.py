# Foster Garcia
# AIST 2120: Programming Assignment 5
# 04/21/2023

# Imports modules


import os, re, csv, sys, json


# Creating directory path


homeFolder = 'C:\\'
userDir = 'garci\\OneDrive'
desktopPath = os.path.join(homeFolder,'Users',userDir,'Desktop')
os.chdir(desktopPath)


# Welcome banner


print()
print('--------------------------------'.center(60))
print('---        AIST 2120         ---'.center(60))
print('---   Progamming Assignment 5   ---'.center(60))
print('---     CSV and JSON Files    ---'.center(60))
print('--------------------------------'.center(60))
print()


print()
print('**********       MOUNTAINEER DOGS      **********'.center(60))
print('*******                                      *******'.center(60))
print('*****   ANNUAL SALARY CALCULATIONS AND PROCESSNG    *****'.center(60))


print()
print("The current wokring directory is ... " + str(desktopPath))
print()


print("BEGIN PROCESSING .....")


# Opens text file in read mode and complies a regex


empInfo = open('EmpInfCur.txt', 'r')
matches = []
correctRegex = []
sqlRegex = re.compile(r'\D+[*,]\D+[;]\D?')


for line in empInfo:

    '''Reads each line of a given text file

    Stores regex matches inside a list

    Stores the corrected text
    '''

    matches += sqlRegex.findall(line)
    correctRegex = re.sub("\D+[*,]\D+[;]\D?","",line.strip("\n"))


print()


for x in matches:

    # Tells user that SQL code has been romoved

    print('=>FOUND SQL Injection: ' + x)
    print('SQL Removed')


print()


fileLines = []
with open('EmpInfCur.txt','r') as file:

    # Opens text file and appends employee name and salary

    lines = file.readlines()

    for line in lines[1:]:
        fileLines.append(line.split()[-1])
        fileLines.append(line.split()[0])


print(fileLines)


print()


with open('EmpPayApr2023.csv', 'w', newline='') as file:

    # Writes employee information to CSV file

    csvWriterObj = csv.writer(file)

    csvWriterObj.writerow(["NAME", "CUR SAL", "BONUS", "TOTAL COMP"])
    csvWriterObj.writerows(fileLines[3:3])


# Reads CSV file


csvReaderObj = csv.reader('EmpPayApr2023.csv')

print(csvReaderObj)

stringOfJsonData = '{"Month":4,"Day":21,"Year":2023}'

jsonDataAsPythonValue = json.dumps(stringOfJsonData)

with open("TimeDate.json", "w") as file:
    file.write(jsonDataAsPythonValue)

print()
print("*** SALARY OPERATIONS for 04/2023 COMPLETE ***")
print()

sys.exit()