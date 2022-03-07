class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def right(self):
        return f'{self.name} повернула направо'

    def left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'{self.name} едет со скоростью {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print('{self.name} едет со скоростью {self.speed}')
        if self.speed > 60:
            return f'{self.name} превышает допустимую сокрость'
        else:
            return f'{self.name} едет со скоростью {self.speed}'



class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print('{self.name} едет со скоростью {self.speed}')
        if self.speed > 40:
            return f'{self.name} превышает допустимую сокрость'
        else:
            return f'{self.name} едет со скоростью {self.speed}'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

lamborghini = SportCar(150, 'красный', 'lamborghini', True)
bmw = TownCar(60, 'черный', 'bmw', True)
mazda = WorkCar(80, 'белый', 'mazda', False)
mercedes = PoliceCar(70, 'синий',  'mercedes', False)

print(lamborghini.show_speed())
print(bmw.show_speed())
print(mazda.show_speed())
print(mercedes.show_speed())
print(lamborghini.left())
print(bmw.right())
print(f'{mazda.name} имеет {mazda.color} цвет')
print(f'{bmw.name} относится к классу town car {bmw.is_police}')

