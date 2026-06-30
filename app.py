import os
import json

file_path = "data/karvands.json"
INITIAL_DATA = {"bootcamp":{"title":"AI-Bootcamp", "year":"2026"}, "karvands":[]}

def initialize_data():
    
    if not os.path.exists("data"):
        os.mkdir("data")
    if not os.path.exists(file_path):
        with open(file_path, "w") as file :
            json.dump(INITIAL_DATA, file) 




def main():
    initialize_data()


if __name__ == "__main__":
    main()