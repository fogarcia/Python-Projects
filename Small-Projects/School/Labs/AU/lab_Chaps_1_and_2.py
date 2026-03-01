# Foster Garcia
# AIST 2120 Lab 1 (Chapters 1 and 2)
# 01/18/2023

# Originiated by Steve Weldon.  Updated by UCA Justin Henry, 5/2021.

# ********************************************************************
# WELCOME to your first lab. This lab is broken into two parts.  The
# first will explore type casting and string concatenation; the second
# will work with prompting for user input and working with an imported
# module.  Let's get started.
# ********************************************************************

# These red colored lines are comments. Comments are denoted with a '#'.

# Welcome Banner

print()
print('--------------------------------'.center(60))
print('---        AIST 2120         ---'.center(60))
print('---      Lab Exercise 1      ---'.center(60))
print('---       Hello World+       ---'.center(60))
print('--------------------------------'.center(60))
print()


#-----------------------------------------------------------------------
# This first section deals with data types and casting.  We will need
# some variables, so I will start by creating them for you! DO NOT CHANGE!

user_var = ''
var_1 = '50'
var_2 = '25'
var_3 = '10'

print('variable 1 is ' + var_1)
print('variable 2 is ' + var_2)
print('variable 3 is ' + var_3)
print()


# I have my variables, but since they are strings, I can't do any 
# arithmetic operations on them!  FIX the code below so that the math is
# correct!  Watch out for the tricky variables in the print statements.

output_1 = int(var_1) + int(var_2) + int(var_3)

print('output 1 is the sum: ' + str(int(output_1)))
print()


# Now do the same using floats.

output_2 = float(var_1) + float(var_2) + float(var_3)

print('output 1 is the sum: ' + str(float(output_2)))
print()


#-----------------------------------------------------------------------
# The next task is to change the value of var_1 to the string 'Hello' 
# and to change the value of var_2 to 'World'.  Do this above the print
# function below.

var_1 = "Hello"
var_2 = "World!"


print(var_1 + ' ' + var_2)
print()


#-----------------------------------------------------------------------
# Now that you have some understanding of data types and how to manipulate
# them, let's move on to accepting input from a user.  We will also import
# our first module and use it.  We will do this by generating pseudo random
# numbers between 0 and 9.  The user will determine the number of times
# random numbers are generated.

print()
print('--------------------------------'.center(60))
print('---         Part 2           ---'.center(60))
print('--------------------------------'.center(60))
print()


# WRITE an import statement below for the random module.

import random


# PROMPT the user to enter an integer below and save the input as user_var.


user_var = input("Enter an integer:")


# This code will help you see what was entered.  DO NOT CHANGE

print('The user entered: ' + user_var + '\nThis was entered as a ' +
      str(type(user_var)))

print()


# Write a for loop to generate the pseudo random numbers between 0 and 9.
#    Use the user_input to determine how many random numbers to generate.
#    This for loop can be found on page 47 of the textbook.
# Ensure user_var is the correct type each place it is used.  
# Add the code below the print statement.
# Print the numbers to the screen.
# Note:  This code would crash without the import statement from earlier.

print('Now printing ' + user_var + ' random numbers!')


for i in range(10):
    print('The next number is ' + str(int(random.randint(0,9))))



#-----------------------------------------------------------------------
# Exit Message

print()
print('--------------------------------'.center(60))
print('---    End Lab Exercise 1    ---'.center(60))
print('--------------------------------'.center(60))
