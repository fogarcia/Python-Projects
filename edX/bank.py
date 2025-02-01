
greeting = input("Greeting:").strip().lower()

if "hello" in greeting:
    print("$0")
elif greeting.startswith("h") and greeting != "hello":
    print("$20")
elif greeting != "hello":
    print("$100")
else:
    print("$0")
