from re import X
from pygame import mixer
mixer.init()
mixer.music.load('alone.mp3')
while True:
    X = input('Perintah: ')
    if X == 'Mainkan':
        mixer.music.play()
    elif X == 'Stop':
        mixer.music.stop()
    elif X == 'Pause':
        mixer.music.pause()
    elif X == 'Unpause':
        mixer.music.unpause()
    else:
        pass
