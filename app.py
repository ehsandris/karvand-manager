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


def save_data(data):
    with open(file_path, "w") as file :
        json.dump(data, file, indent=4)


def load_data():
    with open(file_path, "r") as file :
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print("JSON file is corrupted. A new file has been created.")
            save_data(INITIAL_DATA)
            return INITIAL_DATA
    return data


def get_number(message):
     while True:
          try:
               number = int(input(message))
               return number
          
          except ValueError: 
                print("PLEASE Enter a valid number")
               
          

def add_applicant():
    
    data = load_data()
    applicant_id_list = []

    for applicant in data["karvands"]:
         applicant_id_list.append(applicant["id"])
    if  applicant_id_list:
         applicant_id = (max(applicant_id_list) + 1)
         
    else:
        applicant_id = 1

    full_name = input("Enter name : ").strip().lower()
    email = input("Enter email : ").strip().lower()
    city = input("Enter city : ").strip().lower()

    degree = input("Enter degree : ").strip().lower()
    field = input("Enter field : ")
    education = {"degree": degree, "field": field}

    skills = []
    while True:
        
        skill_name = input("Enter skill name : ").strip().lower()
        skill_level = input("Enter skill level : ").strip().lower()
        skill_score = get_number("Enter skill score between 0 - 100 : ")
        while skill_score < 0 or skill_score > 100:
            print("Score must be between 0 and 100.")
            skill_score = get_number("Enter skill score between 0 - 100: ")
             
        skill = {
            "name": skill_name,
            "level": skill_level,
            "score": skill_score
        }
        skills.append(skill)

        answer = input("Add another skill? (y/n): ").lower().strip()

        if answer == "n":
            break
    new_applicant  = {
        "id": applicant_id,
        "full_name": full_name,
        "email": email,
        "city": city,
        "education": education,
        "skills": skills
    }

    data["karvands"].append(new_applicant)

    save_data(data)
 
def show_applicants():

    data = load_data()

    if not data["karvands"]:
        print("No applicants found.")
        return
    
    for applicant in data["karvands"]:
        count = 1
        print(f"""
----------------------------------------
ID: {applicant["id"]}
Name: {applicant["full_name"]}
Email: {applicant["email"]}
City: {applicant["city"]}

Education
----------
Degree : {applicant["education"]["degree"]}
Field  : {applicant["education"]["field"]}

Skills
------
""")
        for skill in applicant["skills"]:
            
            print(f'{count}. {skill["name"]} ({skill["level"]} - Score: {skill["score"]})')
            count +=1
        print("-" * 40)



def main():
    initialize_data()

    while True:
        print("""
========= Karvand Manager =========

1. Add Applicant
2. Show Applicants
3. Search Applicant by ID
4. Search Applicant by Skill
5. Edit Applicant
6. Delete Applicant
7. Report
0. Exit

===================================
""")
        choice = input("Choose an option: ").strip()

        if choice == "1":
             add_applicant()
             
        elif choice == "2":
             show_applicants()
        
        elif choice == "3":
            pass
             #search_applicant_by_id()
        
        elif choice == "4":
            pass
             #search_applicant_by_skill()
        
        elif choice == "5":
            pass
             #edit_applicant()
        
        elif choice == "6":
            pass
             #delete_applicant()

        elif choice == "7":
            pass
             #report()

        elif choice == "0":
             break
        
        else :
             print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()