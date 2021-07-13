def fibonacci(n):
    if n==1:
        return 0

    elif n==2:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)        

# 0 1 1 2 3 5 8  

num = int(input("Enter  :"))
print(fibonacci(num))        