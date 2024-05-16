class Pet:
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_type(self, animal_type):
        self.animal_type = animal_type

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_type(self):
        return self.animal_type

    def get_age(self):
        return self.age

    @staticmethod
    def get_valid_age_input():
        while True:
            try:
                age = int(input("Enter the pet's age: "))
                return age
            except ValueError:
                print("Invalid! Please enter an integer for the age.")

def main():
    pet_name = input("Enter your pet's name:\n")
    pet_type = input("Enter your pet's type:\n")
    pet_age = Pet.get_valid_age_input()

    my_pet = Pet(pet_name, pet_type, pet_age)

    print(f"\nYour pet name: {my_pet.get_name()}")
    print(f"Your pet type: {my_pet.get_type()}")
    print(f"Your pet age: {my_pet.get_age()}")

if __name__ == "__main__":
    main()