from pathlib import Path
import json

chuck_size = 8192

def sha256(file_path) -> str:
    import hashlib
    h = hashlib.sha256()
    with file_path.open("rb") as f:
        while True:
            chunk = f.read(chuck_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

root = Path.cwd()
current = {}

baseline_file = input("Enter the name of the baseline file (e.g., hashes.json): ").strip()

for p in root.rglob("*"):
    if p.is_file():
        if p.name == baseline_file:
            continue
        relative_path = p.relative_to(root)
        current[str(relative_path)] = sha256(p)

print(f"Current hashes calculated for {len(current)} files.")

with open(baseline_file, "r", encoding="utf-8") as f:
    baseline_hashes = json.load(f)

print(f"Baseline hashes loaded from {len(baseline_hashes)} files.")

baseline_keys = set(baseline_hashes.keys())
current_keys = set(current.keys())

added = sorted(current_keys - baseline_keys)
removed = sorted(baseline_keys - current_keys)
modified = sorted(k for k in baseline_keys & current_keys if baseline_hashes[k] != current[k])

print(f"Added files: {len(added)}")
for f in added:
    print(f"  + {f}")
print(f"Removed files: {len(removed)}")
for f in removed:
    print(f"  - {f}")
print(f"Modified files: {len(modified)}")
for f in modified:
    print(f"  * {f}")