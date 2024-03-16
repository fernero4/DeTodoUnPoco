import webbrowser
import pygame
import pyautogui
import keyboard
import threading
from time import sleep
# webbrowser.open(
#     'https://open.spotify.com/intl-es/track/5qJ1OFXySmyGcs7Sn6r2cf')

url_cancion = 'https://open.spotify.com/intl-es/track/5qJ1OFXySmyGcs7Sn6r2cf'
url_spotify = 'https://open.spotify.com/intl-es/track/5qJ1OFXySmyGcs7Sn6r2cf'


# def reproducir_musica(url_cancion):
#     pygame.mixer.init()
#     pygame.mixer.music.load(url_cancion)
#     pygame.mixer.music
# .play()
#     pygame.event.wait()


def abrir_navegador(url_spotify):
    webbrowser.open(url_spotify, new=2)
    sleep(5)
    keyboard.press_and_release('space')


# reproducir_musica(url_cancion)
abrir_navegador(url_spotify)
