import os
import getpass
import Error


username = getpass.getuser()
path = 'C:\\Users\\{}\\'.format(username)
global file_root, names


def play():
    global file_root, names
    filename = str(input('Lex:\\User\\command\\groove\\title|artist> ')).lower()
    music_list = []
    for root, directories, files in os.walk(path):
        for name in files:
            # for specific file type
            if name.endswith('.mp3'):
                if filename in name.lower().replace('_', ' '):
                    music_list.append(name)
                    print('\n'f'Found in: {root}')
                    print((len(music_list)), ')', name)
                    file_root = root
    if len(music_list) > 1:
        print('\n'f'[SUCCESS]: {len(music_list)} music found for {filename}.')
        choice = int(input('Lex:\\User\\command\\play\\{}\\choice|return[0]> '.format(filename)))
        for music_name in music_list:
            try:
                if choice == music_list.index(music_name) + 1:
                    directory = (os.path.join(file_root, music_name))
                    os.startfile(directory)
                elif 0 == choice:
                    break
            except FileNotFoundError:
                Error.printline('[ERROR|Music]: File unavailable.\n')
    elif len(music_list) == 1:
        print('\n'f'[SUCCESS]: {len(music_list)} music found for {filename}.')
        choice = int(input('Lex:\\User\\command\\play\\{}\\choice|return[0]> '.format(filename)))
        for music_name in music_list:
            try:
                if choice == music_list.index(music_name) + 1:
                    directory = (os.path.join(file_root, music_name))
                    os.startfile(directory)
                elif 0 == choice:
                    break
            except FileNotFoundError:
                Error.printline('[ERROR|Music]: File unavailable.\n')
    else:
        Error.printline('[ERROR|Music]: 0 file found.\n')
