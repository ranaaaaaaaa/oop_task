# add_car()
# remove_car()
# park_car()
# display_available_spots()
# Use Encapsulation to hide the data - e.g. total capacity and available spots should be private attributes.

class Garage:
    # __init__ is where you set up the object's starting data.
    def __init__(self):
        self.total_capacity = 5
        self.__capacity= 5
        self.__spots= 5
        self.parked_cars = []
        self.added_cars = []

    def display_available_spots(self):
        print(f"You have {self.total_capacity - len(self.added_cars)} spots left.")

    def add_car(self, new_car):
        if self.__capacity != 0 :
            self.__capacity= self.__capacity - 1
            self.added_cars.append(new_car)
            print("Car added successfully.")
        else :
            print("Not enough capacity.")


    def park_car(self, new_car):
        # park the car if it exists in records and if it doesn't then add it first then park it
        if self.__spots != 0 and self.__capacity != 0 :
            self.__spots= self.__spots - 1
            if new_car not in self.added_cars:
                self.added_cars.append(new_car)
                self.__capacity= self.__capacity - 1
            self.parked_cars.append(new_car)
            print("Car parked successfully.")
        else :
            print("You can't park here!")

    def remove_car(self, new_car):
        # remove the car from the records
        self.added_cars.remove(new_car)
        if new_car in self.parked_cars:
            self.parked_cars.remove(new_car)
            self.__spots = self.__spots + 1
        self.__capacity= self.__capacity + 1
        print("Your Membership ended.")


garage = Garage()

garage.display_available_spots()
garage.add_car("Toyota")
garage.add_car("Honda")
garage.park_car("Toyota")
garage.display_available_spots()
garage.remove_car("Honda")
garage.display_available_spots()
garage.park_car("Mazda")
garage.display_available_spots()