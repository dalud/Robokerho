import vlc
#media = vlc.MediaPlayer("/home/pi/robokerho/samples/video/Unheroic_labours_2_h264.mov")
media = vlc.MediaPlayer("/home/pi/robokerho/samples/video/sample_1280x720_surfing_with_audio.mp4")



while True:
    media.play()
    if media.is_playing(): print("TV:", media.get_time())
