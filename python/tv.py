from videoIF import Video
from wlanIF import Wlan
import sys


# Helpers
flush = sys.stdout.flush

# Init video
video = Video("/home/pi/robokerho/samples/video/Unheroic_labours_2_h264_AdobeCreativeCloudExpress.mp4")
video.play()

# Init Wlan
wlan = Wlan()
flush()

while True:
    if video.time():
        print(video.time(), "(", int(video.time()/60000), ":", int(video.time()%60000/1000), ")")
        wlan.broadcast('TV:' + str(video.time()))
        flush()
