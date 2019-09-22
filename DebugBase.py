#Base Class
class DebugBase:
    def __init__(self, pet_name):
        self.name = pet_name

    def your_pet(self):
        print("Oh no, your pet " + self.name + " ran away!")


