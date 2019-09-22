# Main Class
from DebugInherit import DebugInherit

class DebugMain:

    def main():
        a_cat = DebugInherit("Rexasaur Smith", 5)
        a_cat.meow()
        a_cat.get_age()
        a_dog = DebugInherit("Fido", 10)
        a_dog.bark()
        a_dog.your_pet()
    if __name__ == "__main__":
        main()




