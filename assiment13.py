try:
    with open("name.txt") as f:
        f.read()
except FileNotFoundError:
    print("Error :file not exist")        