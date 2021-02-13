#pin = int("1234")
#supplied_pin = int(input("£nter your pin: "))
#if pin == supplied_pin:
#    print("Thank you. Welcome to your bank account.")
#elif pin != supplied_pin:
#    print("Sorry, that pin was incorrect.")
#    supplied_pin2 = int(input("Enter your pin: "))
#    if pin == supplied_pin2:
#            print("Thank you. Welcome to your bank account.")
#    elif pin != supplied_pin2:
#            print("Sorry that pin was incorrect. You have one more attempt left before you are locked out of your account!")
#            supplied_pin3 = int(input("Enter your pin. Remember this is your last chance!"))
#            if pin == supplied_pin3:
#                    print("Phew! You remembered your pin! Welcome to your bank account")
#            else:
#                    print("Your bank account is now locked. Please contact our support desk to unlock your account.")

import getpass
pin = int("1234")
supplied_pin = int(getpass.getpass(prompt='Please enter your password: '))
if supplied_pin == pin:
    print("Thank you. Welcome to your bank account.")
elif pin != supplied_pin:
    print("Sorry, that pin was incorrect.")
    supplied_pin2 = int(getpass.getpass(prompt='Please enter your password: '))
    if pin == supplied_pin2:
        print("Thank you. Welcome to your bank account.")
    elif pin != supplied_pin2:
        print("Sorry that pin was incorrect. You have one more attempt left before you are locked out of your account!")
        supplied_pin3 = int(getpass.getpass(prompt='Last chance before your account is locked. Please enter your pin: '))
        if pin == supplied_pin3:
            print("Phew! You remembered your pin! Welcome to your bank account")
        elif pin != supplied_pin3:
            print("Your bank account is now locked. Please contact our support desk to unlock your account.")
