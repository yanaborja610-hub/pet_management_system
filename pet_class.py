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

    def display_pet(self):
        print(f"Name: {self.__name}")
        print(f"Animal Type: {self.__animal_type}")
        print(f"Age: {self.__age}")

    def save_to_file(pets):
        with open("pet_records.txt", "a") as file:
            if file.tell() == 0:
                file.write("=" * 60 + "\n")
                file.write(" " * 15 + "PET RECORDS\n")
                file.write("=" * 60 + "\n")

            animal_types = []

            for pet in pets:
                if pet.get_animal_type() not in animal_types:
                    animal_types.append(pet.get_animal_type())

            for animal in animal_types:
                file.write(f"\n{animal.upper()}S\n")
                file.write("-" * 60 + "\n")
                file.write(
                    f"{'PET NAME': <25}"
                    f"{'ANIMAL TYPE': <20}"
                    f"{'AGE': <10}\n"
                )

                file.write("-" * 60 + "\n")

                for pet in pets:
                    if pet.get_animal_type() == animal:
                        file.write(
                            f"{pet.get_name():<25}"
                            f"{pet.get_animal_type():<20}"
                            f"{pet.get_age():<10}\n"
                        )

                file.write("\n")