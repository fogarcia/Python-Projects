# Foster Garcia
# AIST 2120, Lab 3 (Chap. 5)
# 01/25/2021

# Originated by Steven Weldon. Modified by UCA Justin Henry (May 2021)

# **********************************************************************
# In this lab we will work with creating and modifying a dictionary.  
# **********************************************************************

# Welcome Banner

print()
print('--------------------------------'.center(60))
print('---        AIST 2120         ---'.center(60))
print('---      Lab Exercise 3      ---'.center(60))
print('---     Dictionary-inator    ---'.center(60))
print('--------------------------------'.center(60))
print()


# Import pretty print and sys

import pprint
import sys


#-----------------------------------------------------------------------
# Create a function that computes the average grade of the dictionary
# created below.  Use a docstring to describe the purpose
# of this function.
#      HINT: NOTE THE k, v FOR LOOP in the Main program section

def average(x):
	'''Takes in a paramater'''
	avg = 0
	for v in x.values():
		'''Takes the sum of all the values and adds them to "avg"'''
		avg += v 
		'''Takes the avg and then divides it by the length of the dictionary'''
	avg = avg / len(x)
	'''Prints the average to screen'''
	print("\n" + "The student's average accross all classes is: " + str(avg))





# ****** MAIN Program ******


# Create an empty dictionary named my_dictionary

my_dictionary = {}



# Printing the dictionary.  DO NOT CHANGE

print("Here's your empty dictionary:  ")
print(my_dictionary)
print()


# Populate the dictionary with the following key-value pairs:
#       'Calc 2', 97
#       'Data Structures', 82
#       'Operating Systems', 88
#       'Elvish Language - Lord of the Rings', 78,
#       'Raptor Natural History and Captive Management', 95

my_dictionary = {'Calc 2': 97, 'Data Structures': 82, 'Operating System': 88,
'Elvish Language - Lord of the Rings': 78, 'Raptor Natural History and Captive Management': 95}





# Print the keys and values using the items() method.  Compare the output
# of your print statement with your neighbors.  Did they print in the same
# order?  DO NOT CHANGE

print("The dictionary Keys and Values added follow:")

for k, v in my_dictionary.items():
	print('     Key ' + str(k) + ' has Value ' + str(v))
	
print()


# Check to see if 'Automation and Scripting' is in my_dictionary.  Print the
# result.

print("Is 'Automation and Scripting' in the dictionary?")
print('Automation and Scripting' in my_dictionary.keys())
 

## Call the function.  Remember to pass it my_dictionary

average(my_dictionary)
 

# Print the dictionary using 'regular' print().  Place your code after the
# two print statements below.  Notice the escape characters used to double
# space.

print('\n\n')           
print("The regular print of the dictionary follows.")

# Place your code here.

print("\n")
print(my_dictionary)


# Print the keys and values using Pretty Print.  Place your code after the
# two print statements below.
#    Note the difference between this print and the earlier 'regular' print.

print('\n\n')           
print("Here's a Pretty Print of the dictionary -- much better!")

# Place your code here.

print("\n")
pprint.pprint(my_dictionary)

#-----------------------------------------------------------------------
# Exit Message

print()
print('--------------------------------'.center(60))
print('---    End Lab Exercise 5    ---'.center(60))
print('--------------------------------'.center(60))
print()
print()


# Exit the program cleanly by a) prompting the user to press enter; b) then
# calling sys.exit() to pause until after the user presses enter.




#-----------------------------------------------------------------------
# End of Lab Exercise 5
