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



def search_applicant_by_id():
    data = load_data()
    applicant_id = get_number("Enter applicant id : ")

    for applicant in data["karvands"]:
        count = 1
        if applicant_id == applicant["id"]:
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
            
            return

    print("Appllicant not found .")
        
           
def search_applicant_by_skill():
    data = load_data()
    applicant_skill = input("Enter skill : ").strip().lower()
    found = False
    
    for applicant in data["karvands"]:
        count = 1
        for skill in applicant["skills"]:
            if skill["name"] == applicant_skill :
                found = True
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
""")
                for skill in applicant["skills"]:
                
                    print(f'{count}. {skill["name"]} ({skill["level"]} - Score: {skill["score"]})')
                    count +=1
                print("-" * 40)
                break
    if not found:
        print("Applicant not found.")


def edit_applicant():

    data = load_data()
    applicant_id = get_number("Enter applicant id : ")
    found = False

    for applicant in data["karvands"]:
        count = 1
        if applicant_id == applicant["id"]:
            found = True
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
            break    
    if not found: 
        print("Applicant not found.")
        return
             
        
    update_item = get_number("""
What do you want to edit?

1. Full Name
2. Email
3. City
4. Degree
5. Field
6. Skills
0. Cancel
""")
    
    if update_item == 1 :
            print(f"Curent name is : {applicant["full_name"]}")
            new_name = input("Enter new name : ").strip().lower()
            applicant["full_name"]= new_name
            print(f"New name is : {applicant["full_name"]}") 

    elif update_item == 2:
            print(f"Curent email is : {applicant["email"]}")
            new_email= input("Enter new email : ").strip().lower()
            applicant["email"]= new_email
            print(f"New email is : {applicant["email"]}")

    elif update_item == 3:
            print(f"Curent city is : {applicant["city"]}")
            new_city= input("Enter new city : ").strip().lower()
            applicant["city"]= new_city
            print(f"New city is : {applicant["city"]}")

    elif update_item == 4:
            print(f"Curent education degree is : {applicant["education"]["degree"]}")
            new_degree= input("Enter new degree : ").strip().lower()
            applicant["education"]["degree"]= new_degree
            print(f"New degree is : {applicant["education"]["degree"]}")

    elif update_item == 5:
            print(f"Curent education field is : {applicant["education"]["field"]}")
            new_field= input("Enter new field : ").strip().lower()
            applicant["education"]["field"]= new_field
            print(f"New field is : {applicant["education"]["field"]}")

    elif update_item == 6:
            count = 1
            skill_found = False
            for skill in applicant["skills"]: 
                print(f'{count}. {skill["name"]} ({skill["level"]} - Score: {skill["score"]})')
                count +=1
            new_skill = input("Which one : ").lower().strip()
            for skill in applicant["skills"]:
                if new_skill == skill["name"]:
                    skill_found = True
                    skill["name"]= input("Enter new skill name :").strip().lower()
                    skill["level"]= input("Enter new skill level :").strip().lower()
                    skill["score"]= get_number("Enter new skill score between 1 - 100 : ")
                    while  skill["score"] < 0 or skill["score"] > 100:
                        print("Score must be between 0 and 100.")
                        skill["score"] = get_number("Enter skill score between 0 - 100: ")
                    print("Skill updated !")
                    break
            if not skill_found:
                print("Skill not found.")
                return
                 
    elif update_item == 0:   
            return
    
    else:
        print("Invalid option.")
        return

    save_data(data)

    print("Applicant updated successfully.")


def delete_applicant():

    data = load_data()
    applicant_id = get_number("Enter applicant id : ")

    for applicant in data["karvands"]:
        count = 1
        if applicant_id == applicant["id"]:
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
            
            user_accept = input("Are you sure? (y/n)").strip().lower()
            if user_accept == 'y':
                data["karvands"].remove(applicant)
                save_data(data)
                print("Applicant deleted successfully.")
                return
            else : 
                print("Deletion canceled.")
                return
    
    
    print("Applicant not found.")
    
    

def report():
    data = load_data()
    total_karvands = len(data["karvands"])
    skill_names_list = []
    skill_score_list = []
    applicant_cities_list = []

    for applicant in data["karvands"]:
        for skill in applicant["skills"]:
            skill_names_list.append(skill["name"])
            skill_score_list.append(skill["score"])
    
        applicant_cities_list.append(applicant["city"])

    if skill_score_list:
        average_skill_score = round((sum(skill_score_list) / len(skill_score_list)), 2)
    else :
        average_skill_score = 0

    report = {
    "total_karvands": total_karvands,
    "total_skills": len(skill_names_list),
    "average_skill_score": average_skill_score,
    "cities": sorted(list(set(applicant_cities_list))),
    "unique_skills": sorted(list(set(skill_names_list)))
}

    with open("data/report.json", "w") as file :
         json.dump(report, file, indent=4)

    
    print(f"""
----------------------------------------
Total karvands : {total_karvands}
Total skills : {len(skill_names_list)}
Avg skills score : {average_skill_score}
cities : {sorted(list(set(applicant_cities_list)))}
Unique skills : {sorted(list(set(skill_names_list)))}
----------------------------------------
""")
        

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
             search_applicant_by_id()
        
        elif choice == "4":
             search_applicant_by_skill()
        
        elif choice == "5":
             edit_applicant()
        
        elif choice == "6":
             delete_applicant()

        elif choice == "7":
             report()

        elif choice == "0":
             break
        
        else :
             print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
        

        