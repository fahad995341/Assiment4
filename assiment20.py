try:
    with open("text2.txt") as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("Error : file nahi mille!")
finally:
    print("file handling completed.")            