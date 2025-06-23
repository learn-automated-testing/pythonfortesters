# Classes and Objects - Foundation for Automation Frameworks

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
    
    def start_engine(self):
        self.is_running = True
        print(f"{self.brand} {self.model} engine started")
    
    def stop_engine(self):
        self.is_running = False
        print(f"{self.brand} {self.model} engine stopped")
    
    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"

# Creating objects
my_car = Car("Toyota", "Camry", 2020)
print(my_car.get_info())
my_car.start_engine()

# Inheritance - Important for Page Object Model
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity
        self.charge_level = 100
    
    def charge(self, percentage):
        self.charge_level = min(100, self.charge_level + percentage)
        print(f"Charged to {self.charge_level}%")
    
    def get_info(self):
        return f"{super().get_info()} (Electric, {self.battery_capacity}kWh)"

tesla = ElectricCar("Tesla", "Model 3", 2023, 75)
print(tesla.get_info())
tesla.charge(20) 