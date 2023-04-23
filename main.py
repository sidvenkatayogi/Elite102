import query

currentAcc = ()
on = True
access = False

while on:
    print(" __________________________")
    print("| Welcome to ELITE BANKING!| ")
    print(" --------------------------")
    print(" > SIGN IN         (1)")
    print(" > CREATE ACCOUNT  (2)")
    print(" > EXIT            (3)")
    welcome = int(input("What do you want to do? "))
    if welcome == 1:
        while not access:
            print(" ---------SIGN-IN----------")
            accName =    input("     Name:  ")
            accPin = int(input("     PIN:   "))
            if query.getAcc(accName, accPin) != False:
                currentAcc = query.getAcc(accName, accPin)
                print("     ACCESS GRANTED\n")
                print(f"     Welcome {accName} !")
                access = True
            else:
                # print(" *INVALID CREDENTIALS*")
                print("    *SIGN IN FAILED*")

        while access:
            print(" \n-----------MENU-----------")
            print(" > CHECK BALANCE   (1)\n")
            print(" > DEPOSIT MONEY   (2)\n")
            print(" > WITHDRAW MONEY  (3)\n")
            print(" > EDIT ACCOUNT    (4)\n")
            print(" >     SIGN OUT    (5)")
            print("---------------------------")

            choice = int(input("What would you like to do? >  "))

            if choice == 1:
                print("\nTOTAL BALANCE:  $" + str(query.getBalance(currentAcc[0])))
            elif choice == 2:
                damount = int(input("How much money would you like to deposit? >  "))
                query.deposit(damount, currentAcc[0])
                print(f"\n*SUCCESSFULLY DEPOSITED ${damount}!*")
            elif choice == 3:
                wamount = int(input("How much money would you like to withdraw? >  "))
                query.withdraw(wamount, currentAcc[0])
            elif choice == 4:
                edit = True
                while edit:
                    print("\n--------ACCOUNT-INFO----------")
                    print(f" > NAME:  {currentAcc[1]}  (1)")
                    print(f" > EMAIL: {currentAcc[3]}  (2)")
                    print(f" > PIN:   {currentAcc[2]}       (3)\n")
                    print( " >     *CLOSE ACCOUNT*     (4)")
                    print(f" >       BACK TO MENU      (5)")

                    choice2 = int(input("\nWhat would you like to edit? >  "))

                    if choice2 == 1:
                        name = input("\n New Name: ")
                        query.editName(name, currentAcc[0])
                        currentAcc = query.getAcc(name, currentAcc[2])
                    elif choice2 == 2:
                        email = input("\n New Email: ")
                        query.editEmail(email, currentAcc[0])
                        currentAcc = query.getAcc(currentAcc[1], currentAcc[2])
                    elif choice2 == 3:
                        pin = int(input("\n New PIN: "))
                        query.editPin(pin, currentAcc[0])
                        currentAcc = query.getAcc(currentAcc[1], pin)
                    elif choice2 == 4:
                        delete = input("            \n*ALERT*\nAre you sure you want to delete your account? (Y/N) >  ")
                        if delete == "Y":
                            query.closeAcc(currentAcc[0])
                            print("*Account Deleted.*")
                            currentAcc = ()
                            edit = False
                            access = False
                    elif choice2 == 5:
                        edit = False

            elif choice == 5:
                currentAcc = ()
                access = False
    elif welcome == 2:
        print("\nWe're glad you want to create an account! Enter the following information to get started.")
        name = input("Name:  ")
        pin = int(input("PIN:  "))
        email = input("Email:  ")
        dep = int(input("How much do you want your initial deposit to be? >  "))
        query.createAcc(name, pin, email, dep)
        print("SUCCESSFULLY CREATED ACCOUNT!")
        print(f"Welcome to Elite Banking {name} !")
    elif welcome == 3:
        on = False
print("\nThank you for choosing Elite Banking! We hope to see you again!")


