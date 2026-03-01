# Foster Garcia
# AIST 2120, Lab 4 (Chap. 7)
# 02/13/2023

# Created by UCA Justin Henry

# **********************************************************************
# For this lab I will create the phone regex; then you will create
# the email and date RegExes.
# **********************************************************************


# Welcome Banner

print('------------------------------------'.center(60))
print('---          AIST 2120           ---'.center(60))
print('---   Lab Exercise 4 (Chap. 7)   ---'.center(60))
print('---         REGEX RUMBLE         ---'.center(60))
print('------------------------------------'.center(60))
print()
print()
print('WELCOME TO REGEX RUMBLE!' .center(60))
print()


#--------------------------------------------------------------------------
# Import pyperclip and re

import pyperclip, re


# ****** MAIN Program ******


# This is the phone RegEx. It is set for (XXX)-XXX-XXXX  DO NOT CHANGE.

pReg = re.compile(r'\d{3}-\d{3}-\d{4}')


# Now create two of your own regexes. One for email addresses and another
# for dates.
# The dates will follow the MM/DD/YYYY format. Note that some dates may not
# need to use all of their possible characters.  For example, 1/1/2021 fits the
# format, but would get missed by a RegEx looking for MM/DD/YYYY EXPLICITLY.

eReg = re.compile(r'[a-zA-Z0-9-_]*\w+@\w+\.[a-z]{3}')
dateReg = re.compile(r'\d{,2}\/\d{,2}\/\d{,4}')





# Now, the .txt file needs to be checked using the regexes we created. I will
# give you the one for phone numbers to get you started.
# Remember to copy the search file to the clipboard before running the program.

info = str(pyperclip.paste())

matchlist = []

matchObject = pReg.findall(info)

print()
print('Phone numbers:')

for x in matchObject:
    print(x)
    
print()


# Now that you have been given this example, search the text on the 
# clipboard for emails and dates using your own regexes. Print the
# results to the screen.

print ('\nHmmm ... I wonder what\'s significant about the dates.') # DO NOT CHANGE.

#Date search

info = str(pyperclip.paste())

matchDateList = []

matchDate = dateReg.findall(info)

print()
print('Dates:')

for x in matchDate:
    print(x)
    
print()

#Email search

info = str(pyperclip.paste())

matchEmailList = []

matchEmail = eReg.findall(info)

print()
print('Emails:')

for x in matchEmail:
    print(x)
    
print()
print("Dates meaning:")

print("The Marine Corps was formed on 11/10/1775"+
"\nThe Attack of Pearl Harbor took place on 12/7/1941"+
"\nThe WWII D-Day invasion of Normandy took place on 6/6/1944")

# IMPORTANT!: If you did not highlight the text in the file and Ctrl+C
# it to the clipboard, you will have no output
















#--------------------------------------------------------------------------
# End banner

print()
print('--------------------------------'.center(60))
print('---    End Lab Exercise 4    ---'.center(60))
print('--------------------------------'.center(60))






