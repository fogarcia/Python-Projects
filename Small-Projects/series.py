# Foster Garcia
# AIST 2120, PA 1 - Ch. 3
# 01/28/2023

#Program which calculates memory usuage of a virus.

# Loop which validates user input.

while True:

    user_input = input("How many seconds (integer) has the computer virus been replicating: ")

    # Checks for negative integers & non-numeric characters

    try:
        user_input = int(user_input)
    except:
        print("Input must be numeric. Please reenter input.")
        continue

    if user_input < 0:
        print("Cannot use negative values. Reenter a positive integer or zero to continue.")
        continue
    break

def virus_calculator(user_int):

    """Uses user input to calculate the amount of bytes of memory a virus is using."""

    count = 0
    global virus
    virus = 1024
    print("\n" + "Calculating virus memory after " + str(user_int) + " seconds.")

    # Loop which doubles the virus and keeps count of loop interations.

    while(count != user_int):
        virus *= 2
        count += 1
        print("\t" + "At t+" + str(count) + ", memory calculation doubles to " + str(virus))

    print("\n \t" + "Viral memory utilization calculation complete!")

# ****** MAIN Program ****** 

virus_calculator(user_input)

print("\n" + "The virus is using " + str(virus) + " bytes of memory.")