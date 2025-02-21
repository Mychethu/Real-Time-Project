import subprocess

# Replace with actual file names
files_to_run = ["C:/Users/chethan/OneDrive/Desktop/Project/sign language recognition system/signup_page.py", "C:/Users/chethan/OneDrive/Desktop/Project/sign language recognition system/login_page.py", "C:/Users/chethan/OneDrive/Desktop/Project/sign language recognition system/test.py"]

for file in files_to_run:
    subprocess.run(["python", file])
