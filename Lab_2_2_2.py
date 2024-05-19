class PhoneNumber:
    def __init__(self, area_code, number):
        self.area_code = area_code
        self.number = number

    def __str__(self):
        return f"{self.area_code}-{self.number}"

class UserType:
    ENGINEER = 1
    MANAGER = 2

    @staticmethod
    def get_type_name(user_type):
        if user_type == UserType.ENGINEER:
            return "Engineer"
        elif user_type == UserType.MANAGER:
            return "Manager"
        else:
            return "Unknown"

class User:
    def __init__(self, name, age, user_type, phone_number):
        self.name = name
        self.age = age
        self.user_type = user_type
        self.phone_number = phone_number

class UserDetails:
    def __init__(self, user):
        self.user = user

    def print_details(self):
        print("Name:", self.user.name)
        print("Age:", self.user.age)
        print("Type:", UserType.get_type_name(self.user.user_type))
        print("Phone:", self.user.phone_number)

# Пример использования классов
phone = PhoneNumber("050", "9379992")
user = User("John", 25, UserType.ENGINEER, phone)
user_details = UserDetails(user)
user_details.print_details()
