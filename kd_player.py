import pygame

class KDPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.current = None

    def load(self, path):
        self.current = path
        pygame.mixer.music.load(path)

    def play(self):
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()

def kd_info():
    return "Mini zenelejátszó KD készítésében – saját modul, osztály, függvény ✔"
