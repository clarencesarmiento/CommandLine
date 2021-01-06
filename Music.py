import os
import random
from pygame import mixer
import getpass
import Error

username = getpass.getuser()
music_list = []
path = 'C:\\Users\\{}\\Music\\'.format(username)


def play_music(text):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.mp3'):
                names = (os.path.join(root, file))
                music_list.append(names)
                if 'list' in text:
                    file_name = names.split(str(root))[-1].strip()
                    print(file_name)
                elif 'play' in text:
                    symbols = ['-', '_']
                    for s in symbols:
                        mixer.init()
                        music = text.split('play')[-1].strip().replace(' ', s)
                        if music in names.lower():
                            mixer.music.load(names)
                            return mixer.music.play()
                        else:
                            pass
                elif 'random' in text:
                    number = random.randint(0, len(music_list))
                    name = (os.path.join(root, files[number]))
                    mixer.init()
                    mixer.music.load(name)
                    return mixer.music.play()
                elif 'pause' in text and 'unpause' not in text:
                    return mixer.music.pause()
                elif 'unpause' in text:
                    return mixer.music.unpause()
                elif 'stop' in text:
                    return mixer.music.stop()
                else:
                    return Error.printline(f'[ERROR]: {text} is not available.\n')
