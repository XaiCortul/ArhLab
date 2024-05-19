class PhoneNumber:
    def __init__(self, code, number):
        self.code = code
        self.number = number
    
    def __str__(self):
        return f"{self.code} {self.number}"

class User:
    type_engineer = 1
    type_manager = 2    

    def __init__(self, name, age, type, phone_number):
        self.name = name
        self.age = age
        self.type = type
        self.phone_number = phone_number

    def print_details(self):
       
        print("Name:", self.name)
        print("Age:", self.age)
        print("Type:", "Engineer" if self.type == self.type_engineer else "Manager")
        print("Phone:", self.phone_number)


phone = PhoneNumber("050", "9379992")
user = User("John", 25, User.type_engineer, phone)
user.print_details()
