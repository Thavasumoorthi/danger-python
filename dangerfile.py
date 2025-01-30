from danger_python.danger import danger

# Check if PR title is too short
if len(danger.github.pr_title) < 10:
    danger.fail("❌ PR title is too short! Must be at least 10 characters.")

# Check if PR has a description
if not danger.github.pr_body:
    danger.warn("⚠️ PR description is missing. Please add a meaningful description.")
