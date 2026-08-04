import os
import shutil

# Source aur Destination folder
source = r"C:\Users\mrshi\OneDrive\Pictures\Camera Roll"
destination = r"C:\Users\mrshi\JPG_Files"

# Destination folder agar nahi hai to bana do
if not os.path.exists(destination):
    os.makedirs(destination)

# Saari JPG files move karo
for file in os.listdir(source):
    if file.lower().endswith(".jpg"):
        shutil.move(
            os.path.join(source, file),
            os.path.join(destination, file)
        )

print("✅ All JPG files moved successfully!")