def game():
    UserInput = input('Are you ready?')
    if "yes" or "y" or "ye" == UserInput:
        print('working')
    else:
        UserExitInput = input("Are you sure you want to exit")
        if UserExitInput == "yes" or "y" or "ye":
            sys.exit()
        else:
            game()


game()
input()
