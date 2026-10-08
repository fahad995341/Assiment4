import os
if os.path.exists("text2.txt"):
    os.remove("text2.txt")
    print("file deleted")
else:
    print("file not found")


