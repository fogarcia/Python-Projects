# Foster Garcia
# AIST 2120: Programming Assignment 6
# 04/29/2023


# Imports modules & password
import os, sys, json, zipfile, PyPDF2, time, pprint


pdfPass = 'enigma'


# Creating desktop directory path
homeFolder = 'C:\\'
userDir = 'garci\\OneDrive'
desktopPath = os.path.join(homeFolder,'Users',userDir,'Desktop')
os.chdir(desktopPath)


# Creating secret in path, secret out path, and PA6 path
sInPath = os.path.join(homeFolder,'Users', userDir, 'Desktop', 'PA6 Files', 'Secret_In')
sOutPath = os.path.join(homeFolder,'Users', userDir, 'Desktop', 'PA6 Files', 'Secret_Sent')
paPath = os.path.join(homeFolder,'Users', userDir, 'Desktop', 'PA6 Files')


print()
print("Ensured current dir is the Desktop: " + os.getcwd())
print()


print("Unzipping files . . .")
print()


print('Change into "PA Files" dir. completed: ' + paPath)
print()


zipObj = zipfile.ZipFile('PA6_Archive.zip', 'r')
status = zipObj.extractall(desktopPath)


print('==> Input Files sent by CONTROL')


for dir, folder, files, in os.walk(sInPath):

    '''Walks through every folder and directory

    Prints the name of the folder and files
    '''

    # For loop that walks though each folder
    for foldername in folder:
        print(folder)

    # For loop that walks throuhg each file
    for filename in files:
        print('\t' + filename)


print()


# Encrypting the first PDF file
start = time.time()


os.chdir(sInPath)


pdfFile = open('Shannon_1938.pdf', 'rb')


os.chdir(sOutPath)


# Intilaizing pdf reader/writer objects
pdfReader = PyPDF2.PdfReader(pdfFile)
pdfWriter = PyPDF2.PdfWriter()


# For loop that reads every page of a PDF file
for pageNum in range(len(pdfReader.pages)):
    pdfWriter.add_page(pdfReader.pages[pageNum])


pdfWriter.encrypt(pdfPass)


resultPDF = open('encrypted_Shannon_1938.pdf','wb')


pdfWriter.write(resultPDF)


resultPDF.close()
pdfFile.close()


end = time.time()


# Calculates time of execution for first PDF encrpytion
result = round(end - start, 2)


# Encryption of second PDF
start2 = time.time()


os.chdir(sInPath)


pdfFile2 = open('Turing_Paper_1936.pdf', 'rb')


os.chdir(sOutPath)


pdfReader2 = PyPDF2.PdfReader(pdfFile2)
pdfWriter2 = PyPDF2.PdfWriter()


# For loop that reads every page of a PDF file
for pageNum in range(len(pdfReader2.pages)):

    # Reads every page of a PDF file
    pdfWriter2.add_page(pdfReader2.pages[pageNum])


pdfWriter2.encrypt(pdfPass)


resultPDF2 = open('encrypted_Turing_Paper_1936.pdf','wb')


pdfWriter2.write(resultPDF2)


resultPDF2.close()
pdfFile2.close()


end2 = time.time()


# Calculates time of execution for second PDF encrpytion
result2 = round(end2 - start2, 2)


# Encryption of third PDF
start3 = time.time()


os.chdir(sInPath)


pdfFile3 = open('Turing_Paper_1950.pdf', 'rb')


os.chdir(sOutPath)


pdfReader3 = PyPDF2.PdfReader(pdfFile3)
pdfWriter3 = PyPDF2.PdfWriter()


# For loop that reads every page of a PDF file
for pageNum in range(len(pdfReader3.pages)):
    pdfWriter3.add_page(pdfReader3.pages[pageNum])


pdfWriter3.encrypt(pdfPass)


resultPDF3 = open('encrypted_Turing_Paper_1950.pdf','wb')


pdfWriter3.write(resultPDF3)


resultPDF3.close()
pdfFile3.close()


# End time of PDF encrpytion
end3 = time.time()


# Calculates time of execution for third PDF encrpytion
result3 = round(end3 - start3, 2)


print('=> Encrypted PDF files ready to send to Mr. Peabody:')


for path, dirc, files in os.walk(sOutPath):
    '''Walks through every folder and directory of 

    sOutPath and prints the name of the files ending

    in an .pdf extension
    '''
    for filenames in files:
        if filenames.endswith('.pdf'):
            print('\t' + filenames)


print()
print('=> Time to process each secret PDF:')


os.chdir(paPath)


# Stores the execution results in a dictionary
timeDic = {'Shannon_1938.pdf': result, 'Turing_Paper_1936.pdf': result2, 'Turing_Paper_1950.pdf': result3}


pprint.pprint(timeDic)


# Writes the time dictionary to a JSON file
stringOfJsonData = json.dumps(timeDic)


# Creates a JSON file in write mode
with open("time_fileFG.json", "w") as outfile:
    outfile.write(stringOfJsonData)


print()
print('JSON time_file created and placed in ' + paPath)
print()


print("*** ALL CONTROL FILES PROCESSING COMPLETE ***".center(60))
print()


# Exit module
sys.exit("Enter any key to exit:")


# Bonus
'''Bonus: Enigma was a new form of encryption that used computing power.

It was developed by the Germans in WWII as a way to encode messages.

The machine porcess was able to produce 160 billion million cipher

combinations using an electro-machanical cipher machine.

All these ciphers use to be produced by hand until the advent of

an enigma machine.
'''