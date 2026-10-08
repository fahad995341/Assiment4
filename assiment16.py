student = {
    "name" :"fahad",
    "age" : 23
}

try:
    print(student["fname"])
except KeyError:
    print("Error : Key not found.")    