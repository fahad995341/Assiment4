cal = 0
with open("numbers.txt") as f :
    for line in f:
        line = line.strip()
        if line:
            numbers = int(line)
            cal += numbers
print(f"cal sum :{cal}")            