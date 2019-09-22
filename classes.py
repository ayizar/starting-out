from MyPet import MyPet

class MyDog(MyPet):
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume
    def bark(self):
        if self.volume > 3:
            print("Woof woof woof")
        else:
            print("Yip yip yip")

small_dog = MyDog("Pup", 2)
big_dog = MyDog("Coco", 5)

small_dog.bark()
big_dog.bark()