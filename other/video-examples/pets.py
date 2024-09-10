class Pet():
    def __init__(self, name, age, spay_or_neutered, deceased):
        self.name = name
        self.age = age
        self.spay_or_neutered = spay_or_neutered
        self.deceased = deceased
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")
    
    def speak(self):
        print("I don't know what I say")
        
class Dog(Pet):
    
    def speak(self):
        print("Bark")

    def roll_over(self, count):
        for i in range(count):
            print("Roll over")

class Cat(Pet):
    # Adding a new property
    number_of_lives = 9
    
    # Overriding the speak method
    def speak(self):
        print("Meow")

def create_dog() -> Dog:
    dog = Dog("Rex", 5, True, False)
    return dog

def create_cat() -> Cat:
    cat = Cat("Whiskers", 3, True, False)
    return cat

def create_pet(cat_or_dog: str) -> Pet:
    if cat_or_dog == "cat":
        return create_cat()
    elif cat_or_dog == "dog":
        return create_dog()
    else:
        return None
        
if __name__ == "__main__":
    # Create a dog object
    print(f'Creating a dog object')
    print('---------------------')
    rex = create_dog()
    rex.show()
    rex.speak()
    rex.roll_over(3)
    print()
    
    # Create a cat object
    print(f'Creating a cat object')
    print('---------------------')
    whiskers = create_cat()
    whiskers.show()
    whiskers.speak()
    print(whiskers.number_of_lives)
    print()
    
    # Create a dog object using the create_pet function
    print(f'Creating a dog object using the create_pet function')
    print('----------------------------------------------------')
    pet = create_pet("dog")
    pet.show()
    pet.speak()
    print()
    
    # Create a cat object using the create_pet function
    print(f'Creating a cat object using the create_pet function')
    print('----------------------------------------------------')
    pet2 = create_pet("cat")
    pet2.show()
    pet2.speak()
    print()
