a  = int(input("Enter : "))
b = (input("Enter 1 or 0 : "))
i=0

if b == "1":
    for i in range (0 , a+1) :
        print("*" * int(i))
    # while i < a :
    #     print("*" * (i+1))
    #     i=i+1

if b =="0":
    for i in range (a,0,-1):
        print("*" * int(i))
