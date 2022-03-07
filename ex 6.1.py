import time

class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def running(self):
        color = 0
        while color < 3:
            print('Светофор переключается на ' f'{TrafficLight.__color[color]}')
            if color == 0:
                time.sleep(7)
            elif color == 1:
                time.sleep(2)
            elif color == 2:
                time.sleep(10)
            color += 1


TrafficLight = TrafficLight()
TrafficLight.running()
