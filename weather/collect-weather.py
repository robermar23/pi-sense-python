from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    sleep(5)
    myfile = open('weather.txt', 'a')
    myfile.write(str(sense.get_temperature()))
    myfile.write('\n')
    myfile.close()