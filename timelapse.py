import os
from os import system
import datetime
from time import sleep

tlminutes = 60
secondsinterval = 120
fps = 1 
numphotos = int((tlminutes*60)/secondsinterval)
print("number of photos to take = ", numphotos)

dateraw = datetime.datetime.now()
datetimeformat = dateraw.strftime("%Y-%m-%d_%H:%M:%S")
print("Webcam started taking photos for your timelapse at: " + datetimeformat)

system('rm /home/pi/Pictures/*.jpg')

for i in range(numphotos):
    os.system('fswebcam -r 1280x720 -S 9 --jpeg 90 --save /home/pi/Pictures/%Y-%m-%d_%H:%M:%S.jpg')
    sleep(secondsinterval)
    
print("Done taking photos")
print("Please standby as your timelapse video is created.")

system('ffmpeg -r {} -f image2 -s 1280x720 -nostats -loglevel 0 -pattern_type glob -i "/home/pi/Pictures/*.jpg" -vcodec libx264 -crf 2  -pix_fmt yuv420p /home/pi/Videos/{}.mp4'.format(fps, datetimeformat))

print('Timelapse video is complete. Video saved as /home/pi/Videos/{}.mp4'.format(datetimeformat))
