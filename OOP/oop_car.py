class Car:
    color = 'black'
    transmission = 'manual'
    gear_position = 'N'

    def __init__(self, transmission):
        self.transmission = transmission
        print('Engine is ready!')

    def drive(self):
        self.gear_position = 'D'
        print('Drive')

    def reverse(self):
        self.gear_position = 'N'
        print('Reverse. Please check your behind.')

    def change_gear(self, gear):
        self.gear_position = gear
        print('Gear positiion on: ' + self.gear_position)

    def get_gear_position(self):
        self.gear_position
        return

car1 = Car('manual')
car1.change_gear('D-1')
car1.reverse()

car2 = Car('automatic')
gear_position = car2.get_gear_position()
print(gear_position)

# class Tesla(Car):
#     pass # use 'pass' keyword to define
# class only
# tesla = Tesla('automatic')
# tesla.drive()

class Tesla(Car):
    def drive(self):
        super().drive()
        print('LOL Gas')