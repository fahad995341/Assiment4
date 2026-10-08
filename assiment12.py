try:
    user = int(input("Enter number only :"))
    print(f"your number {user}")
except ValueError:    
    print("Value error!")
