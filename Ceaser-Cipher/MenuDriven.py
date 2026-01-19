
choice = ''
while(choice != '0'):
    choice = input("Enter '1' for Encryption \nEnter '2' for Decryption: \nEnter '0' to Exit: \n")
    if choice == '1':
        from Encryption import *

    elif choice == '2':
        sub_choice = input("Enter '1' for Decryption: \n"
                       "Enter '2' for Bruteforce Decryption using Dictionary: \n"
                       "Enter '3' for Frequency Analysis based Decryption: \n"
                        "Enter '0' to Exit: \n" )
        if sub_choice == '1':
            from Decryption import *
        elif sub_choice == '2':
            from Bruteforce_dictionary import *
        elif sub_choice == '3':
            from Frequency import *
        elif sub_choice == '0':
            exit()
        else:
            print("Invalid choice for Decryption.")
            exit()
    elif choice == '0':
        exit()
    else:
        print("Invalid choice.")
        exit()


