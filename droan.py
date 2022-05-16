
#flips don't work right now

from djitellopy import tello
from time import sleep

tello = tello.Tello()
tello.connect

#launch

tello.takeoff()
sleep(1)

#move up 90cm

tello.move_up(90)
sleep(1)

#flip forward

#tello.flip_forward()
#sleep(1)

#move forward 800cm

tello.move_forward(400)
tello.move_forward(400)
sleep(1)

#flip backward

#tello.flip_back()
#sleep(1)

#turn left 90

tello.rotate_counter_clockwise(90)
sleep(1)

#move forward 400cm

tello.move_forward(400)
sleep(1)

#flip left

#tello.flip_left()
#sleep(1)

#turn left 90

tello.rotate_counter_clockwise(90)
sleep(1)

#move forward 800cm

tello.move_forward(400)
tello.move_forward(400)
sleep(1)

#flip right

#tello.flip_right()
#sleep(1)

#turn left 90

tello.rotate_counter_clockwise(90)
sleep(1)

#move forward 400cm

tello.move_forward(400)
sleep(1)

#land

tello.land()
