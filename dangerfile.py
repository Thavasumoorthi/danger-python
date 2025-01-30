# Dangerfile.py
from danger import Danger, fail, warn, message

danger = Danger()

# Example: Check for new files > 1KB
for file in danger.git.created_files:
    if danger.utils.file_size(file) > 1000:
        fail(f"Large file detected: {file} (>1KB)")

# Example: Warn if PR has no description
if not danger.github.pr.body:
    warn("Please add a description to this PR")