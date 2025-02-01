def convert(input):
    if input.find(":)"):
        input = input.replace(":)", "🙂")
    if input.find(":("):
        input = input.replace(":(", "🙁")
    print(input)


def main():
    user_input = input("")
    convert(user_input)

main()


