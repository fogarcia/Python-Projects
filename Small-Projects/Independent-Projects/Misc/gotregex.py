#Foster Garcia
#AIST 2120, PA 2 - Ch. 7
#02/17/2023

# Imports for pyperclip, re, and sys

import re
import pyperclip as pyip
import sys




# Header

print()
print("***** MOUTAIN DOGS EMPLOYEE EMERGENCY CONTACT LIST *****".center(60))
print()
print("This report contains employ emergency contact information obtained from HR data.")
print()




# *****MAIN PROGRAM*****

"""Program which searches for specificed regexes within a document

If no information is found prompts the user stating no information was found
"""




# Name, phone, date regexes created

nameReg = re.compile(r'[A-Z]\D+\s+[A-Z]\D+\W')

phoneReg = re.compile(r'''\d{3}[-\.\s]?\d{3}[-\.\s]?\d{4}\s*ext\.\s?\d{,5}|
                        \d{3}[-\.\s]?\d{4}\s*ext\.\s?\d{,5}|
                        \d{3}[-\.\s]?\d{4}|
                        \d{3}[-\.\s]?\d{3}[-\.\s]?\d{4}
                        ''')

dateReg = re.compile(r'\d{,2}[\/-]\d{,2}[\/-]\d{,4}')

print("==> BEGIN REPORT")
print()


info = str(pyip.paste())

matchList = []

matchObj = nameReg.findall(info) + phoneReg.findall(info) + dateReg.findall(info)

if len(matchObj) > 0:
    for x in matchObj:
        print("".join(x))
else:
    print("\t***No employee contact information was found***"
          +"\n\tCheck with HR to verify correct file information.")

print()


print("\t==> REPORT COMPLETE")



# Footer

print()
print('-------------------------------------------'.center(60))
print('---    END of Programming Assignment 2    ---'.center(60))
print('-------------------------------------------'.center(60))



# Historical significance bonus

print("""Grace Hopper was born on December 9th 1906.

Hopper is best known for her involvment with the UNIVAC system, which was the first electronic digital computer.

Edsger Dijkstra was a computer scientist who solved the graph-theory problem, which is finding the shortest path between two nodes.

Dijkstra solved the problem sitting in a cafe in under 20 minutes.
""")




# System exit prompt

input("Press enter to exit program.")
sys.exit()