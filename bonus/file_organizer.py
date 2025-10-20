import os, shutil, pathlib

folder = r"C:\Users\ravikumar\Downloads"  # Change to your folder path

for file in os.listdir(folder):
    path = os.path.join(folder, file)
    if os.path.isfile(path):
        ext = pathlib.Path(file).suffix[1:] or "Others"
        target_dir = os.path.join(folder, ext.upper())
        os.makedirs(target_dir, exist_ok=True)
        shutil.move(path, os.path.join(target_dir, file))

print("✅ Files organized successfully!")