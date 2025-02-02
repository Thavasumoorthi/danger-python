from danger_python import Danger, markdown

danger = Danger()

# Get the PR titles
title = danger.github.pr.title
markdown(f"PR Title: {title}")

    markdown("✅Danger -python working fine")



# Check if any files contain 'TODO'
todo_files = []

# Loop through changed files and check for 'TODO'
for file in danger.github.pr.changed_files:
    if 'TODO' in file.content:
        todo_files.append(file.filename)

# Display a warning if any TODOs are found
if todo_files:
    markdown("⚠️ Files with 'TODO' found:")
    for file in todo_files:
        markdown(f"- {file}")
else:
    markdown("✅ No TODOs found in the changed files.")
