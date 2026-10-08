with open ("numbers.txt","a") as f:
    num = 0
    for i in range(1,6):
        num = f"{i}\n" 
        data = f.write(num)   