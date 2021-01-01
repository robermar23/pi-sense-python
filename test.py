from sense_hat import SenseHat
import time

sense = SenseHat()

#show a message
sense.show_message("DICKS ")
#sense.low_light = True

# set pixles through array of arrays
X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

question_mark = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

sense.set_pixels(question_mark)


# set pixels at specific x,y coordinate
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# examples using (x, y, pixel)
#sense.set_pixel(0, 0, red)
#sense.set_pixel(0, 1, green)
#sense.set_pixel(0, 2, blue)

time.sleep(2)

#sense.show_letter("A")

#time.sleep(5)

sense.low_light = False

#sense.show_message("Environment")

temp = sense.get_temperature()
sense.show_message("Temperature: %s C" % temp)
