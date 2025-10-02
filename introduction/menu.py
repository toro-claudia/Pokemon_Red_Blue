from intro import Introduction
import time

class Menu:
    def __init__(self):
        lines = [ 
        "************************************************************",
        "*                                                          *",
        "*                  POKEMON RED & BLUE                      *",
        "*                                                          *",
        "************************************************************"
        ]        

        for line in lines:
            print(line)
            time.sleep(0.2)
            
        input("\nPress ENTER to continue")

        menu = [ 
        "************************************************************",
        "*                          MENU                            *",
        "*                    SELECT 1: LOGIN                       *",
        "*                    SELECT 2: MAKE ACCOUNT                *",
        "*                                                          *",
        "************************************************************"
        ] 

        for line in menu:
            print(line)

        select = int(input())
        
        if select == 1:
            print("work in progress")
        elif  select == 2:
            game = Introduction()
            game.create_profile()

game = Menu()