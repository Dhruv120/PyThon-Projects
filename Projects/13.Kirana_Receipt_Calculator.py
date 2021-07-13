items_list = {"biscuit" :50 , "cake" :100 , "chocolate": 30 }
bill = 0
print("Welcome to Kirana.com")
print('''This is our menu :
 1 - biscuit
 2 - cake
 3 - chocolate
''')

while (True):
    user_input = input("Enter name of item : ")
    
    if (user_input != "ok"):
        quantity = int(input("Enter The Quantity : "))
        bill = bill + (int(items_list[user_input]) * quantity)
        print(f"Order total so far {bill}")

    else:
        print(f"Your total bill is {bill}")    
        print("Thank You for shopping")
        break


 