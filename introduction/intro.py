import json

class Introduction:
    def create_profile(self):
        print("Hello! Welcome to our version of Pokemon Red and Blue, a text-style inspired version from the original nostalgic game we know and love.")
        name = ""
        while(name == ""):
            name = input("\nTo start, please enter your name: ")
            password = input(f"Nice to meet you {name}! Please enter your password: ")

        self.name = name
        self.password = password

        player_data = {
            "player_name": self.name,
            "player_pass": self.password
        }
        with open("player_data.json", "w", encoding= "utf-8") as write_file:
            json.dump(player_data, write_file)
            
    ''' 
    def login(self):
        while(user != player_data(user))
        user = input("\nEnter your username: ")
        password = input("\Enter your password: ")
    '''
intro = Introduction()

    