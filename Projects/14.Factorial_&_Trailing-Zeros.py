def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def factorialTrialZeros(n):
    count = 0
    i = 5
    while(n//i !=0 ):
        count += int(n/i)  
        i = i*5
    return count            

if __name__ == "__main__":
    num = int(input("Enter : "))
    fac = factorial(num)
    print(f"The Factorial of number is {fac}")
    print(factorialTrialZeros(num))
    