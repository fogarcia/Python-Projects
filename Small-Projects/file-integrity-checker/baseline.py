import hashlib
from pathlib import Path

root = Path.cwd()
chuck_size = 8192

print(f"Root directory: {root}")

def sha256(file_path) -> str:
    h = hashlib.sha256()
    with file_path.open("rb") as f:
        while True:
            chunk = f.read(chuck_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

count = 0

for file in root.rglob("*"):
    if file.is_file():
        relative_path = file.relative_to(root)
        digest = sha256(file)
        print(f"{relative_path}: {digest}")
        count += 1

print(f"Total number of files: {count}")