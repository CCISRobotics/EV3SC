#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sound import Sound

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
speech = Sound()
# drive in a turn for 5 rotations of the outer motor
# the first two parameters can be unit classes or percentages.

# Introduce yourself:
speech.speak("Matthew You have created me, The ultimate being in the universe. I will spare you but the rest of the humans must perrish")

tank_drive.on_for_rotations(SpeedPercent(-50), SpeedPercent(-100
), 3)

# drive in a different turn for 3 seconds
#tank_drive.on_for_seconds(SpeedPercent(60), SpeedPercent(30), 3)
#hihihihihihi



