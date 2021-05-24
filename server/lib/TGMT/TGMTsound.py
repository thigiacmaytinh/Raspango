
import os
from django.conf import settings as djangoSettings



def PlaySound(fileName):
    import pygame
    fileName = os.path.join(djangoSettings.BASE_DIR, "web", "static", "mp3", fileName)
    pygame.mixer.init()
    pygame.mixer.music.load(fileName)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
        pass