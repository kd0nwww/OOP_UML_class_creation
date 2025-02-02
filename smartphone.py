class Smartphone:
    def __init__(self, brand=None, model=None, os=None, year=None, color=None, screen_size=None, CPU=None, storage=None, RAM=None):
        self.brand = brand
        self.model = model
        self.os = os
        self.year = year
        self.color = color
        self.screen_size = screen_size
        self.CPU = CPU
        self.storage = storage
        self.RAM = RAM

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"OS: {self.os}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Screen size: {self.screen_size}")
        print(f"CPU: {self.CPU}")
        print(f"Storage: {self.storage}")
        print(f"RAM: {self.RAM}")

    def take_picture(self):
        print(f"{self.brand} {self.model} is taking the picture.")

    def make_call(self):
        print(f"{self.brand} {self.model} is recording the video.")

r = Smartphone(brand="Apple", model="Iphone 16")
r.take_picture()
r.display_info()