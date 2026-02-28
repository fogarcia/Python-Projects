import hashlib
import json
from pathlib import Path

root = Path.cwd()
chuck_size = 8192
baseline_file = input("Enter the name of the baseline file (e.g., hashes.json): ").strip()

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

results = {}

for file in root.rglob("*"):
    if file.name == baseline_file:
        continue
    if file.is_file():
        relative_path = file.relative_to(root)
        digest = sha256(file)
        results[str(relative_path)] = digest
        print(f"{relative_path}: {digest}")
        count += 1

print(f"Total number of files: {count}")
print("Dict entries:", len(results))

with open("hashes.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4)

print("Hashes saved to hashes.json")