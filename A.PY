class PersonalDetails: 
    def __init__(self, name, middle_name, last_name, age, height, weight, subject): 
        self.name = name 
        self.middle_name = middle_name 
        self.last_name = last_name 
        self.age = age 
        self.height = height 
        self.weight = weight 
        self.subject = subject 

    def display_details(self): 
        print("The personal details are:") 
        print(f"Name: {self.name}") 
        print(f"Middle Name: {self.middle_name}") 
        print(f"Last Name: {self.last_name}") 
        print(f"Age: {self.age}") 
        print(f"Height: {self.height}") 
        print(f"Weight: {self.weight}") 
        print(f"Subject: {self.subject}") 

person = PersonalDetails("Pragyan", "Ranjan", "Karn", 12, 152.4, 41, "Mathematics") 
person.display_details()

personal_details_tuple = tuple(vars(person).values())
personal_details_list = list(personal_details_tuple)
print(personal_details_list)