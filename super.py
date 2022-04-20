class Jedi(object):
    def __init__(self, lightsaber_color):
        print(f"I'm a jedi with {lightsaber_color}  lightsaber")


class Yoda(Jedi):
    def __init__(self):
        print("I'm Yoda.")
        super().__init__('Dog')


yoda = Yoda()