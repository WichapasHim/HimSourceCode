
choice=None
while True:
   
    if choice=='0':
        break
    elif choice in '12345':
        print(" You chose {}".format(choice))
    else:
        print("""Please choose your option from the list below:
        1. Learn Python
        2. Learn Java
        3. Go swimming
        4. Have dinner
        5. Go to bed
        0. Exit""")
     choice=input()