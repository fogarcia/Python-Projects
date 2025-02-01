file = input("File name:").lower().strip()

if file.endswith(".jpeg") or file.endswith(".jpg"):
    print(f"image/jpeg")
elif file.endswith(".gif"):
    print(f"image/gif")
elif file.endswith(".png"):
    print(f"image/png")
elif file.endswith(".pdf"):
    print(f"application/pdf")
elif file.endswith(".txt"):
    print(f"text/plain")
elif file.endswith(".zip"):
    print(f"application/zip")
else:
    print("application/octet-stream")

