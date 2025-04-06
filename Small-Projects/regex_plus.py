# Foster Garcia
# AIST 2120: PA 4 - Ch. 10
# 03/13/2023

# Header

print('--------------------------------------'.center(60))
print('---           AIST 2120            ---'.center(60))
print('---   Programming Assignment 4    ---'.center(60))
print('---          Regex plus          ---'.center(60))
print('--------------------------------------'.center(60))
print()


print('  *** MOUNTAIN COMMUNCATIONS COMPANY ***   '.center(60))
print('  ***       IP ADDRESS ANALYSIS      ***   '.center(60))
print()


# Importing modules


import re, zipfile, os


# Prompt user


userOutput_File = input("Enter an output file: ")


# Vaildate user input


vaild = False

while(vaild == False):
    # Only passes .txt files

    if(userOutput_File.endswith('.txt')):
        vaild = True

    else:
        # Reprompts user if invaild

        print("Please enter a text file.")
        userOutput_File = input("Enter an output file: ")
        continue


# Changing directory to the PA4 location


homefolder = "/"

userDir = "garci/OneDrive"

desktopPath = os.path.join(homefolder, "Users", userDir, 'Desktop', 'PA4')

os.chdir(desktopPath)


# Creating IP regex


ipRegex = re.compile(r'''\d{3}\.\d{3}\.\d{3}\.\d{3}''')


# Creating date regex


dateRegex = re.compile(r'''\d{,2}[\/]\d{,2}[\/]\d{,4}|\d{,2}[\-]\d{,2}[\-]\d{,4}''')


# Creating email regex


emailRegex = re.compile(r'''[\w}\.[\w]+@[\w]+\.\D+''')


# Opens logfile in read mode & prints file name to screen


log_File = open('MCCLog.txt', 'r')

print('\nThe input log file is ' + log_File.name + '.')

output_File = open(userOutput_File, 'w')

text = log_File.read()


# Report starts here


print("\n===> BEGIN IP REPORT <===\n")


if len(text) > 0:

    '''Report that prints regexes to screen

    Writes the regex values in user specified document

    Prompts user if no date is found
    '''

    storeRegex = []

    for email in emailRegex.findall(text):
        storeRegex.append(email)
        output_File.write(email + "\n")

    for date in dateRegex.findall(text):
        storeRegex.append(date)
        output_File.write(date + "\n")

    for ip in ipRegex.findall(text):
        storeRegex.append(ip)
        output_File.write(ip + "\n")
    
    for i in storeRegex:
        print(f"{i}")

else:

    print("\t===> No IP data found <===")


print("\n--> End Report <--")

# Closes the output file


output_File.close()


# Start of archiving process


print("\n---Archiving .txt files...")


zipLog = zipfile.ZipFile("output.zip", "w")


# For loop to iterate through all folders, subfolders, and files


for folderName, subfolders, filenames in os.walk(r'C:\Users\garci\OneDrive\Desktop\PA4'):
    zipLog.write(folderName)

    '''Walks through the directory 

    Prints the .txt that are being archived to screen

    Archives the .txt files
    '''

    for filename in filenames:
        if(filename.endswith(".txt")):
            print("\t" + filename)

        zipLog.write(filename)


print("\n" + "   ---Archiving complete.***")


#  Closes archive file


zipLog.close()