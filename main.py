#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

axle_track = 120
wheel_diameter = 55

robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)


# Write your program here.
ev3.speaker.beep()

# Select target from right to left side of plate
target = 4

if target == 1:

    # turn right 50 degrees
    robot.drive_time(0, 48, 1000)

    # go forward
    robot.drive_time(2000, 0, 2000)

    # turn left 85 degrees
    robot.drive_time(0, -85, 1000)

elif target == 2:

    # turn right
    robot.drive_time(0, 16, 1000)

    # go forward
    robot.drive_time(2000, 0, 3000)

    # turn right
    robot.drive_time(0, 65, 1000)

elif target == 3:

    # turn left
    robot.drive_time(0, -45, 1000)

    # go forward
    robot.drive_time(5000, 0, 2000)

elif target == 4:

    # turn right
    robot.drive_time(0, -85, 1000)

    # go forward
    robot.drive_time(2000, 0, 2400)

    # turn right
    robot.drive_time(0, 87, 1000)
