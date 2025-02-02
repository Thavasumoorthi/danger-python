from danger import danger, fail, warn, message

# Example check for PR description
if not danger.github.pr.body:
    fail("❌ Please add a description to your PR.")

# Example check if PR adds more than 500 lines of code
if danger.github.pr.additions > 500:
    warn("⚠️ Big PR detected. Consider splitting it into smaller parts.")

# Example: Find TODO comments in Python files
for file in danger.git.modified_files:
    if file.endswith(".py"):
        with open(file, 'r') as f:
            content = f.read()
            if "TODO" in content:
                message(f"📝 Found TODO in `{file}`")
