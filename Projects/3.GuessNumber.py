actual = 49
attemp = 0


while True :
    attemp +=1
    num1 = int(input("Enter your number :"))
    if num1 > actual :
        print("The number is too high")
 
    elif num1 < actual :
        print("The number is too low") 

    else :
        print(f"you have gussed the number in {attemp} attempt ") 
        break
print("thank you for playing") 