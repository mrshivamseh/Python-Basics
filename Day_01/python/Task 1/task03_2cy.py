import re

# Input file jisme emails hain
with open("data.txt", "r") as f:
    text = f.read()

# Regex se emails nikalna
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Save to new file
with open("emails.txt", "w") as f:
    for email in emails:
        f.write(email + "\n")

print("✅ Emails extracted and saved to emails.txt")
