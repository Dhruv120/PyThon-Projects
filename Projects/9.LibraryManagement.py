class Library:

    def __init__(self , list , name ):
        self.booklist = list
        self.libraryname = name
        self.lendDict = {}

    def displaybook(self):
        print(f"We have the following book in our library : {self.libraryname}")
        for book in self.booklist:
            print(book)        

    def lendbook(self , book , user):
        if book not in self.lendDict.keys():
            self.lendDict.update ({book:user})
            print("Your book has been updated . You can take the book")
        else :
            print(f"Your bokk is already been used by {self.lendDict[user]}")    


    def addbook(self , book):
        self.booklist.append(book)
        print("Book has been successfully added")

    def returnbook(self , book):
        self.lendDict.pop(book)

if __name__ == "__main__":
    dhruv = Library(["anabela" , "emma" , "python" , "c++ basics"] , "Dhruv")

    while (True):
        print("welcome to the dhruv library" )
        print("Please enter your choice")
        print("1 . Display book")
        print("2 . Lend book")
        print("3 . Add book")
        print("4 . Return book")
        user_choice = input("Enter your choice :")
        if user_choice not in ['1','2','3','4']:
            print("Please enter valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            dhruv.displaybook()

        elif user_choice == 2:
            book = input( "Enter the name of book you want to lend : ")
            user = input("Enter your name :")  
            dhruv.lendbook(user , book)

        elif user_choice == 3:
            book = input( "Enter the name of book you want to add : ")
            dhruv.addbook(book)
             

        elif user_choice == 4:
            book = input( "Enter the name of book you want to return : ")
            dhruv.returnbook(book)
             

        else:
            print("Enter valid input")   

        print("Press Q to quit and C to continue") 
        user_choice2 = ""
        while (user_choice2 != "C" and user_choice2 != "Q"):
            user_choice2 = input("Enter Your Choice :")
            if user_choice2 == "Q":
                exit()
            elif user_choice2 == "C" :
                continue    
