from videoIF import Video
from wlanIF import Wlan
import sys
from time import sleep


# Helpers
flush = sys.stdout.flush

# Init video
video = Video("/home/pi/robokerho/samples/video/Unheroic_labours_2_h264_AdobeCreativeCloudExpress.mp4")

# Init Wlan
wlan = Wlan()
flush()

# Play video
def play():
    global video
    
    if not video.is_playing():
        video.play()
        print("Nyt mie laitoin sen käyntiin")
        sleep(1)

    while video.is_playing():
        print(video.time(), "(", int(video.time()/60000), ":", int(video.time()%60000/1000), ")")
        if video.time():
            wlan.broadcast('TV:' + str(video.time()))
            flush()
            sleep(.5)
        if video.get_position() > .98:
            video.stop()


#Main loop
while True:
    hear = wlan.listen()
    
    if hear and 'VIDEO' in hear[0].decode(): play()
