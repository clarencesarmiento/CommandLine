from datetime import date
import Cdate
import datetime
import pyowm
import webbrowser
import wolframalpha
import wikipedia
import subprocess
import os
import getpass
import Error
import MusicPlayer as Player
username = getpass.getuser()
client = wolframalpha.Client('7TYLQ9-HU2TVH2J8Y')
owm = pyowm.OWM('ff388bfc7ea3dfe38a2375b708e752aa')


def info():
    today = date.today()
    now = datetime.datetime.now()
    time_12hour_format = now.strftime('%I:%M %p').lstrip("0")
    loc = owm.weather_manager().weather_at_place('Batangas')
    weather = loc.weather
    temp = weather.temperature(unit='celsius')
    status = weather.detailed_status
    cleaned_temp_data = int(temp['temp'])
    return print(f'\n{Cdate.day_of_week(today.weekday())} {Cdate.month_today(today.month)} {today.day},{today.year}\n'
                 f'Time: {time_12hour_format}\n'
                 f'Temperature: {cleaned_temp_data} degree celsius\n'
                 f'Status: {status}')


def search(text):
    query = text
    try:
        try:
            res = client.query(query)
            result = next(res.results).text
            return print(f'[RESULT|Wolframalpha]: {result}')
        except StopIteration:
            result = wikipedia.summary(query, sentences=2)
            return print(f'[RESULT|Wikipedia]: {result}')
    except wikipedia.exceptions.DisambiguationError:
        url = "https://google.com/search?q=" + query
        return webbrowser.get().open(url)


def google(text):
    query = text
    url = "https://google.com/search?q=" + query
    return webbrowser.get().open(url)


def microsoft(text):
    if 'word' in text:
        try:
            return subprocess.Popen(r'C:\Program Files (x86)\Microsoft Office\root\\Office16\WINWORD.EXE')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE')
    elif 'powerpoint' in text or 'ppt' in text:
        try:
            return subprocess.Popen(r'C:\Program Files (x86)\Microsoft Office\root\\Office16\POWERPNT.EXE')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE')
    elif 'excel' in text:
        try:
            return subprocess.Popen(r'C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE')
    elif 'pub' in text or 'publisher' in text:
        try:
            return subprocess.Popen(r'C:\Program Files (x86)\Microsoft Office\root\\Office16\MSPUB.EXE')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files\Microsoft Office\root\Office16\MSPUB.EXE')
    elif 'outlook' in text:
        try:
            return subprocess.Popen(r'C:\Program Files (x86)\Microsoft Office\root\\Office16\OUTLOOK.EXE')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE')
    elif 'onenote' in text:
        try:
            return subprocess.Popen(r'C:\Program Files (x86)\Microsoft Office\root\\Office16\ONENOTE.EXE')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files\Microsoft Office\root\Office16\ONENOTE.EXE')
    elif 'access' in text:
        try:
            return subprocess.Popen(r'C:\Program Files (x86)\Microsoft Office\root\\Office16\MSACCESS.EXE')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files\Microsoft Office\root\Office16\MSACCESS.EXE')
    else:

        return Error.printline(f'[ERROR]: {text} not available.\n')


def applications(text):
    if 'chrome' in text or 'google' in text:
        try:
            return subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    elif 'discord' in text:
        return subprocess.Popen(r'C:\Users\{}\AppData\Local\Discord\app-0.0.308\Discord.exe'.format(username))
    elif 'windows explorer' in text:
        return subprocess.Popen(r'C:\Windows\explorer.exe')
    elif 'premiere' in text:
        try:
            return subprocess.Popen(r'C:\Program Files\Adobe\Adobe Premiere Pro 2020\Adobe Premiere Pro.exe')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files (x86)\Adobe Premiere Pro 2020\Adobe Premiere Pro.exe')
    elif 'pycharm' in text:
        try:
            return subprocess.Popen(r'C:\Program Files\JetBrains\PyCharm Community Edition 2020.2.1\bin\pycharm64.exe')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files (x86)\JetBrains\PyCharm Community Edition '
                                    r'2020.2.1\bin\pycharm64.exe')
    elif 'steam' in text:
        try:
            return subprocess.Popen(r'C:\Program Files\Steam\steam.exe')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files (x86)\Steam\steam.exe')
    elif 'cad' in text:
        try:
            return subprocess.Popen(r'C:\Program Files\Autodesk\AutoCAD 2019\acad.exe')
        except FileNotFoundError:
            return subprocess.Popen(r'C:\Program Files (x86)\Autodesk\AutoCAD 2019\acad.exe')
    elif 'groove' in text:
        Player.play()
    else:
        return Error.printline(f'[ERROR]: {text} is not available.\n')


def take_note():
    text = str(input('Lex:\\User\\note\\text> '))
    current_date = datetime.datetime.now()
    file_name = str(current_date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    return subprocess.Popen(["notepad.exe", file_name])


def computer(text):
    if 'documents' in text:
        return os.startfile(r'C:\Users\{}\Documents'.format(username))
    elif 'downloads' in text:
        return os.startfile(r'C:\Users\{}\Downloads'.format(username))
    elif 'pictures' in text:
        return os.startfile(r'C:\Users\{}\Pictures'.format(username))
    elif 'music' in text:
        return os.startfile(r'C:\Users\{}\Music'.format(username))
    elif 'videos' in text:
        return os.startfile(r'C:\Users\{}\Videos'.format(username))
    else:
        return Error.printline(f"[ERROR]: {text} is not available.\n")


def close(text):
    if 'word' in text:
        return os.system('taskkill/f /im WINWORD.EXE')
    elif 'ppt' in text or 'powerpoint' in text:
        return os.system('taskkill/f /im POWERPNT.EXE')
    elif 'excel' in text:
        return os.system('taskkill/f /im EXCEL.EXE')
    elif 'pub' in text or 'publisher' in text:
        return os.system('taskkill/f /im MSPUB.EXE')
    elif 'outlook' in text:
        return os.system('taskkill/f /im OUTLOOK.EXE')
    elif 'onenote' in text:
        return os.system('taskkill/f /im ONENOTE.EXE')
    elif 'access' in text:
        return os.system('taskkill/f /im MSACCESS.EXE')
    elif 'browser' in text:
        return os.system('taskkill/f /im chrome.exe')
    elif 'notepad' in text:
        return os.system('taskkill/f /im notepad.exe')
    elif 'discord' in text:
        return os.system('taskkill/f /im Discord.exe')
    elif 'groove' in text:
        return os.system('taskkill/f /im Music.UI.exe')
    else:
        return Error.printline(f'[ERROR]: {text} is not available.\n')
