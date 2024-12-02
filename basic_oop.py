#  a class =- blueprint for creating object = custom data type

class Car: #Pasxal case- HelloThere
    # Constructor - special method that sets up attributes of a new instance
    # will be called sutomatically when a neew instance is created
    def __init__(self, make, model):
        self.__make = make
        self.model = model

    def start(self):
        print(f"{self.__make} {self.model} car started")

    # Function overloading
    def start(self, foo):
        pass


    def __str__(self):
        return f"This is a {self.__make} {self.model}"

# Getter

    def get_make(self):
        return self.__make
    
    # Setter
    def set_make(self, new_make):
        self.__make = new_make

class PetrolCar(Car):
    def __init__(self, make, model, engine, tank_capacity_L):
        super().__init__(make, model)
        self.tank_capacity_L = tank_capacity_L
    
    def __str__(self):
        return f"{super().__str__()}. it has a {self.tank_capacity_L} l tank"
        



# Composition
class Engine:
    def __init__(self, type, max_power_kw, engine):
        self.type = type
        self.max_power_kw = max_power_kw
        self.engine = engine

    def __str__(self):
        return f"This is a {self.type} engine with the max of {self.max_power_kw} kw power "


# Main
engine1 = Engine(type = "petrol", max_power_kw = 235)

my_car = PetrolCar(make = 'honda', model= 'civic', tank_capacity_L = "47", engine = engine1)   #create a new instance of car
# my_car is now an object of class "Car"

your_car = Car("Toyota", "chr")

print(your_car)
# print(my_car.__dict__)
# print(your_car)
# my_car.start()
# your_car.start()

# print(my_car.get_make()) 
print(my_car)
print(your_car)

