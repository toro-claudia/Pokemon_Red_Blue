import json

class introduction:
    def __init__(self):
        print("Hello! Welcome to our version of Pokemon Red and Black, a text-style inspired version from the original nostalgic game we know and love.")

    def create_profile(self):
        name = ""
        while(name != ""):
            name = input("\nTo start, please enter your name: ")
            password = input(f"Nice to meet you {name}! Please enter your password: ")

        self.name = name
        self.password = password

        self.store_data()
    
    def store_data(self):
        player_data = {
            "player_name": self.name,
            "player_pass": self.password
        }
        with open("player_data.json", "w", encoding= "utf-8") as write_file:
            json.dumps(player_data, write_file)

    