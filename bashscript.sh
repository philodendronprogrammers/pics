#!/bin/sh
python /home/pi/GROWONBOOT/Pictures/timelapse.py
git add .
git commit -m "updated"
git push
