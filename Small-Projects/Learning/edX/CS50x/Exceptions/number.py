def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt)) # <--- can return here and it breaks out of the loop as well
            # This code on its own does not allow for strings or chars
            # break # <--- can add break here instead of else
        except ValueError:
            pass
            # print("x is not an integer")
        # else:
        #     break
    # return x
# print(f"x is {x}")

main()