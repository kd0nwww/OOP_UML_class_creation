import os
from smartphone import Smartphone

n = int(input("How many entities you want to create? "))
objects = []

for i in range(n):
        
    brand = input("Enter the brand of your smartphone: ")
    model = input("Enter the model of your smartphone: ")
    operating_system = input("Enter the name of Operating System running on your smartphone: ")
    year = int(input("Enter the year of your smartphone: "))
    color = input("Enter the color of your smartphone: ")
    screen_size = float(input("Enter the screen size of your smartphone(in inches): "))
    CPU  = input("Enter the name of CPU in your smartphone: ")
    storage = int(input("Enter the capacity of storage on your smartphone(in GB): "))
    RAM = int(input("Enter the capacity of RAM on your smartphone(in GB): "))

    os.system("cls")

    object = Smartphone(brand, model, operating_system, year, color, screen_size, CPU, storage, RAM)
    objects.append(object)

for object in objects:
    print("-----" * 5)  # organized output
    object.display_info()
    print("-----" * 5)