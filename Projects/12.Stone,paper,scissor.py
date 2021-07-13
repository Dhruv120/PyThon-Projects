import random


type1 = ["s" , "p" , "sc"]

choice= random.choice(type1)
tchance = 5
noc = 0
cp = 0
hp = 0

while noc < tchance :

    input1  = (input("Enter your choice :"))
    choice= random.choice(type1)
    
    if input1 == type1 :
        print("tie")

    elif input1 == "s" and choice == "sc":
        hp= hp+1
        print("Human win")

    elif input1 == "s" and choice == "p":
        cp= cp+1
        print("Computer win")

    elif input1 == "p" and choice == "sc":
        hp= hp+1
        print("Computer win") 

    elif input1 == "p" and choice == "s":
        hp= hp+1
        print("Human win")

    elif input1 == "sc" and choice == "p":
        hp= hp+1
        print("Human win")             

    elif input1 == "sc" and choice == "s":
        cp= cp+1
        print("Computer win")

    else :
        print("Enter correct input")

    noc = noc +1           

print( f"point of computer :{cp}" )
print( f"point of Human :{hp}" )

if cp > hp :
    print("computer  wins ")    
else :
    print("human wins")    

    