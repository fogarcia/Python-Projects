# Write your solution here 
def spruce(num):

    i = 0

    while i < num:
        if i < num:
            print(f"{'*' * i}*{'*' * i}")
            i += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)