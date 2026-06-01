from pet_class import Pet

pets = []

print("🐾 PET RECORDS 🐾")

number = int(input("How many pets?"))

for i in range(number):
    print(f"\nPet #{i+1}")

    pet = Pet()
    pet.input_pet()
    pets.append(pet)
    pet.save_to_file()