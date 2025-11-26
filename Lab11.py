class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    
    def accelerate(self):
        self.__speed += 5
    
    def brake(self):
        self.__speed -= 5
    
    def get_speed(self):
        return self.__speed


# create a Car object
my_car = Car(2021, "Tesla")

# accelerate the car 5 times and print the speed after each acceleration
for i in range(5):
    my_car.accelerate()
    print("Current speed:", my_car.get_speed())

# brake the car 5 times and print the speed after each brake
for i in range(5):
    my_car.brake()
    print("Current speed:", my_car.get_speed())
