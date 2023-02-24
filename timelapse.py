from picamera import PiCamera
from os import system
from time import sleep
import os
from datetime import datetime

camera = PiCamera()
camera.resolution = (1024, 768)


if((datetime.now().hour<21)and (datetime.now().hour>6) ):
        os.chdir('/home/pi/GROWONBOOT/Pictures')
        camera.capture('image{0:04d}.jpg'.format(i))
        sleep(10800)
        system('convert -delay 5 -loop 0 image*.jpg animation.gif')
        print("captured 1")

camera.close()
system('convert -delay 5 -loop 0 image*.jpg animation.gif')

   # os.chdir('/bin/pictures')

            




