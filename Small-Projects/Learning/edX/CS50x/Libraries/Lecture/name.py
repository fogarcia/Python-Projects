import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
# else:
#     print("hello, my name is", sys.argv[1])

# Print name tags
# for arg in sys.argv[1:-1]:
for arg in sys.argv[1:]:
    print("hello, my name is", arg)

# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")