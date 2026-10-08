try:
    num = int(input("Enter number :"))
    div = 10 / num
    print(div)
except ZeroDivisionError:
    print("Error : 0 se divide nahi kar sakti.")
except ValueError:
    print("Error : only number can allow.")    
