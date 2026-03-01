import sys
import hashlib
from pathlib import Path

chuck_size = 8192

if len(sys.argv) != 2:
    print("Usage: python hash_one.py <filename>")
    sys.exit(1)

path = Path(sys.argv[1])

if not path.is_file():
    print(f"Error: {sys.argv[1]} is not a valid file.")
    sys.exit(1)

h = hashlib.sha256()

with path.open("rb") as f:
    while True:
        chunk = f.read(chuck_size)
        if not chunk:
            break
        h.update(chunk)

print("File found. Calculating hash...")
print(f"SHA-256: {h.hexdigest()}")