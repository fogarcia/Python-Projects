def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Checks if the first two chars are alphabetic
    if s[0:1].isalpha() and s[:].isalnum():
        for i in s[2:3]:
            if i.isdigit() and i != "0" or i.isalpha():
                # Checks the length of s
                if len(s) <= 6 and len(s) >= 2:
                    # Checks if plate ends with a number
                    if s[-1:].isdigit() and s[-2:].isdigit() or s[-1:].isalpha() and s[-2:].isalpha:
                        return True
                    else:
                        return False


main()