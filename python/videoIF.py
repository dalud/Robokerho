import vlc

class Video:
    def __init__(self, media):
        self.media = vlc.MediaPlayer(media)
        print("Media set:", media)

    def play(self):
        #self.media.set_position(.94)
        self.media.play()
        self.media.set_position(0)
        self.media.set_fullscreen(1)

    def time(self):
        if self.media.is_playing(): return self.media.get_time()

    def is_playing(self):
        return self.media.is_playing()

    def get_position(self):
        return self.media.get_position()

    def stop(self):
        self.media.set_pause(1)
