try:
    result = 10/0
    print(result)
except ZeroDivisionError:
    print("Error 0 se divide nahi o sakta.")
finally:
    print("task completed.")#hamesha chaliga chai error ho ya na ho.        