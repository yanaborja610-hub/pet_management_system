class Pet:
    def __init__(self, name = "", animal_type = "", age = 0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    # Getters
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    # For input
    def input_pet(self):
        self.__name = input("Enter pet name: ")
        self.__animal_type = input("Enter animal type: ")
        self.__age = input("Enter age: ")

    def save_to_file(self):
        with open("pet_records.txt", "a") as file:
            file.write(
                f"{self.__name}, "
                f"{self.__animal_type}, "
                f"{self.__age}\n"
            )