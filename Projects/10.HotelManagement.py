class Hotel:

    def __init__(self , room , name):
        self.roomList = room
        self.name = name
        self.Equired = {}

    def allroom(self):
        for room in self.roomList:
            print(room)

    def bookroom(self , room , user) :
        if room not in self.Equired.keys():
            self.Equired.update({room:user})
            print("Room has been alloted to you")
        else:
            print(f"The room is Equired ,  please continue with other room")

    def Checkout(self , room):
        self.Equired.pop(room)



if __name__ == "__main__":
    dhruv = Hotel(["A" , "B" , "C" , "D"] , "Dhruv")

while(True):
    print("Welcome to D- Group of Hotels")
    print("1. display all room") 
    print("2. Book Room")
    print("3. Checkout Room")
    user_choice= int(input("Enter your choice : "))
    if user_choice not in[1,2,3]:
        print("Please enter valid input")
        continue
    else:
        user_choice = int(user_choice)    

    if user_choice == 1:
        dhruv.allroom()

    elif user_choice == 2:
        room = input("Enter your room number : ")
        user = input("Enter your name : ")
        dhruv.bookroom(room , user)

    elif user_choice ==3:
        room = input("Enter your room number : ")
        dhruv.Checkout(room)  

    print("Print Q for Quit and C for Continue")
    choice2 = input("Enter Q / C :")

    if choice2 == "Q":
        exit()
    else :
        continue
