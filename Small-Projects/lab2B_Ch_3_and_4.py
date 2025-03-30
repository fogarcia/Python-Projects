# Foster Garcia
# 01/23/2023
# AIST 2120 Lab 2 (Chapters 3 & 4)

# Originiated by UCA Hunter Thomas.  Updated by UCA Justin Henry, 5/2021.

# **********************************************************************
# In this lab, we will work with some functions that manipulate lists.  
# **********************************************************************

# Welcome Banner

print()
print('--------------------------------'.center(60))
print('---        AIST 2120         ---'.center(60))
print('---      Lab Exercise 2      ---'.center(60))
print('---    Functions and Lists   ---'.center(60))
print('--------------------------------'.center(60))
print()


#-----------------------------------------------------------------------
# Create a function to complete the following tasks:
#    1. Append the number 6 to the list.
#       Print the updated list with 6 appended to it.
#    2. Create a string with your name and capitalize every other letter,
#       e.g. JuStIn HeNrY.  Then print it to the screen.
#    3. Determine the number of capital letters in your name string.
#       Print the number of capital letters in your name string.
#    4. Determine the number of lowercase letters in your name string.
#       Print the number of lowercase letters in your name string.
# This function will be called in a later step.



    # ** Task 1
def myfunction(x):
    x.append(6)
    print("Here is the new list: " + str(x)+"\n")



    # ** Task 2:  The input function is not needed here.  Simply create
    #             the specified string.
mystring = "fOsTeR gArCiA"
print("My input string is " + mystring)


    # ** Tasks 3 and 4:  The 'for' loop is included below to get you started.
    #            started.  Look up the isupper and islower methods to help 
    #            with what goes inside the for loop.  It's up to you to figure
    #            out what else is needed.
lower_counter = 0
upper_counter = 0
for letter_i in mystring:    # DO NOT CHANGE
    if letter_i.islower():
        lower_counter = lower_counter+1
    elif letter_i.isupper():
        upper_counter = upper_counter+1

print(str(int(upper_counter)) + " uppercase letters")        
print(str(int(lower_counter)) + " lowercase letters" + "\n")


# ***** MAIN Program *****

# The initial list is created for you here.  DO NOT CHANGE.

our_list = []                    # Ensures the new list is empty.
for i in range (0,6):
    our_list.append(i)

print('Here is our list: ' + str(our_list))
print()


# Call the function you created.  Remember to pass it the list.

myfunction(our_list)

# Print only the last item of the list.

print("The last item in the list is: " + str(int(our_list[-1])) + "\n")


# Print the length of the list.

print("The length of the list is: " + str(int(len(our_list))) + "\n")



# Remove the second item in the list and print the resulting list.
del our_list[1]
print("New list after deletion: " + str(our_list) + "\n")




# Reverse the list, permanently, and print the result.
our_list.reverse()
print("Reversed list: " + str(our_list) + "\n")




#-----------------------------------------------------------------------
# Exit Message

print()
print('--------------------------------'.center(60))
print('---    End Lab Exercise 2    ---'.center(60))
print('--------------------------------'.center(60))
