# File Intergrity Checker

Baseline and verify a file's intergrity using SHA-256 hashes.

Firstly, creates a baseline using baseline.py within the current directory.

Secondly, uses that baseline (JSON) to compare any additions, deletions, or modifications to directory or files.

## Files

- 'baseline.py' - generates a baseline SHA-256 hash and pushes them to a JSON.
- 'verify.py' - takes that generates JSON and compares changes to the hash.

## Usage

### 1) Create a baseline
'''powershell
python .\baseline.py
# enter: hashes.json

### 2) Verify
'''powershell
python .\verify.py
# enter: hashes.json

Example output:
Enter the name of the baseline file (e.g., hashes.json): hashes.json
Current hashes calculated for 4 files.
Baseline hashes loaded from 3 files.
Added files: 1
  + verify.py
Removed files: 0
Modified files: 1
  * README.md