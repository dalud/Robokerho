import vlc

class Video:
    def __init__(self, media):
        self.media = vlc.MediaPlayer(media)
        print("Media set:", media)

    def play(self):
        self.media.play()
        #self.media.toggle_fullscreen()

    def time(self):
        if self.media.is_playing(): return self.media.get_time()
