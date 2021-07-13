# Recursive way
def factorial(n):
    if n==0 or n==1 :
        return 1
    return n * factorial(n-1)    


fac = factorial(6)
print(fac)



# Iterative way 
# def factorial(n):
#     fac = 1
#     for i in range (n):
#         fac = fac * (i+1)
#     return fac

    
# num = int(input("enter : "))
# print(factorial(num))
 