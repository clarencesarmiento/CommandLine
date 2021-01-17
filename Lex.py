import webbrowser
import os
import tasks
import Music
import schedulefinder as find
import filefinder as f_find
import wifipassword as wp
import Error
from help import help_command


def request():
    user_request = str(input('\nLex:\\User\\command> '))
    return user_request.lower()


print('\nLex Command Line (Version 0.1/Python/November 24, 2020) [Clarence Sarmiento]')
print('Type "-help", "-info" for more information.')
while True:
    command = request()
    if '-help' in command:
        help_command()
    elif '-info' in command:
        tasks.info()
    elif '-wifi' in command:
        wp.wifi_password()
    elif '-sched' in command:
        sched = command.split('-sched')[-1].strip()
        find.schedule(sched)
    elif '-search' in command:
        query = command.split('-search')[-1].strip()
        tasks.search(query)
    elif '-play' in command:
        title = command.split('-play')[-1].strip()
        tasks.youtube(title)
    elif '-file' in command:
        f_find.locate()
    elif '-facebook' in command or '-fb' in command:
        url = "https://www.facebook.com/"
        webbrowser.get().open(url)
    elif '-messenger' in command:
        url = "https://www.messenger.com/"
        webbrowser.get().open(url)
    elif '-gmail' in command:
        url = "https://mail.google.com/"
        webbrowser.get().open(url)
    elif '-google' in command:
        query = command.split('-google')[-1].strip()
        tasks.google(query)
    elif '-classroom' in command:
        url = 'https://classroom.google.com/u/1/h'
        webbrowser.get().open(url)
    elif '-drive' in command:
        url = 'https://drive.google.com/drive/u/0/my-drive?lfhs=2'
        webbrowser.get().open(url)
    elif '-ms' in command:
        ms = command.split('-ms')[-1].strip()
        tasks.microsoft(ms)
    elif '-music' in command:
        music = command.split('-music')[-1].strip()
        Music.play_music(music)
    elif '-access' in command:
        files = command.split('-access')[-1].strip()
        tasks.computer(files)
    elif '-open' in command:
        app = command.split('-open')[-1].strip()
        tasks.applications(app)
    elif '-note' in command:
        tasks.take_note()
    elif '-close' in command:
        app = command.split('-close')[-1].strip()
        tasks.close(app)
    elif '-clear' in command:
        os.system('cls')
    elif '-exit' in command:
        exit()
    else:
        Error.printline('[ERROR]: Unknown Command! Type "-help" for more information.')
