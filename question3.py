class Car:
    def __init__(self ,car_model):
        self.car_model= car_model

    def drive(self):
        print("Driving the car")

    def show_info(self):
        print(self.car_model)

class Battery:
    def charge(self):
        print("Battery is charging.")

    def check_range(self, battery_size):
        print(f"Remaining range is {100 - battery_size}.")

class ElectricCar(Car, Battery):
    def __init__(self, car_model, car_battery):
        super().__init__(car_model)
        self.car_battery = car_battery

    # def check_range(self):
    #     print(f"Remaining range is {100- self.car_battery}.")


my_car = ElectricCar("Tesla Model 3", 75)
my_car.drive()
my_car.show_info()
my_car.charge()
my_car.check_range(20)