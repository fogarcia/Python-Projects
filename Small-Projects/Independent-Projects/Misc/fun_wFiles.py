# Foster Garcia
# AIST 2120: PA 3 - Ch. 9
# 03/04/2023


# Imported modules


import os, re, sys

print("\t\t\t--------------------------------")
print("\t\t\t---        AIST 2120         ---")
print("\t\t\t--- Programming Assignment 3 ---")
print("\t\t\t---      Fun With Files      ---")
print("\t\t\t--------------------------------")


print("\n\n**** WEST VIRGINIA HOT DOGS CONSOLIDATED HIRING: CURRENT WEEK ****")
print("\n\nThe begining CWD is ...",os.getcwd())

WVChas = open("WVDogsChasHR.txt","r")
WVAuburn = open("WVDogsAuburnHR.txt","r")
WVDogsComb = open('WVDogsCombinedHiring.txt', 'a')

print("\n\nHiring files successfully opened. Beginning processing.")


# Erases all date from WVDogsCombinedHiring.txt


WVDogsComb = open('WVDogsCombinedHiring.txt', 'w')

WVDogsComb.close()


print()
print('==> NEW EMPLOYEE INFORMATION <=='.center(60))
print()
print()


print()
print("\n\n\tHiring files validated and written to WVDogsCombinedHiring.txt"
      + "\t\t\tready for processing. All files close.\n\n")
print()


print()
print("Employee Name\t\t\tJob Title\t\t\tSalary or Other Compensation")
print("-------------\t\t\t---------\t\t\t----------------------------")
print()

# Copies data from WVChas file to WVDogsComb file


WVDogsComb = open('WVDogsCombinedHiring.txt', 'w')


for line in WVChas.readlines():
    WVDogsComb.write(line)



# Copies data from WVAuburn to WVDogs comb file and closes WVDogsComb to exit append
# mode and open in WVDogsComb in read mode


for line in WVAuburn.readlines():
    WVDogsComb.write(line)


WVDogsComb.close()

WVDogsComb = open('WVDogsCombinedHiring.txt', 'r')


# Prints WVDogsComb to screen with data


sqlRegex = re.compile(r"[^;]")

matchObj = sqlRegex.findall(line)


for line in WVDogsComb:
    matchObj = sqlRegex.findall(line)
    print(line)


print()
print()
print('------------- HIRING REPORT COMPLETE -------------'.center(60))
print()
print()


print("Press ENTER to exit:")

sys.exit()


# Julia Child bonus

print("""Julia Child was a famous chef that introduced French cuisine to American cooks in 1963. She also was the head
of the Department of Stenograpic Services and worked in Aircraft Warning Services. She also worked for the OSS.""")

