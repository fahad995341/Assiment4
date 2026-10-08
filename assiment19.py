def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or greater.")
    else:
        print("Age is valid")
try:
    check_age("add")
except ValueError as e:
    print(f"Error : {e}")            
    