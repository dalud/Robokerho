from videoIF import Video
from wlanIF import Wlan
import sys


# Helpers
flush = sys.stdout.flush

# Init video
video = Video("/home/pi/robokerho/samples/video/sample_1280x720_surfing_with_audio.mp4")
video.play()

# Init Wlan
wlan = Wlan()
flush()

while True:
    if video.time():
        print(video.time(), "(", int(video.time()/60000), ":", int(video.time()%60000/1000), ")")
        wlan.broadcast('TV:' + str(video.time()))#str(robo.vekeActive(stream)))
        flush()













































































































































