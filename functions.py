import os
import webbrowser
from urllib.parse import quote_plus
import sys
import osascript


def open_disp(voice: str):
    os.system("""osascript -e 'tell app "Activity Monitor" to open'""")
    return voice


def open_settings(voice: str):
    os.system("""osascript -e 'tell app "System Preferences" to open'""")
    return voice


def find_in_internet(voice: str):
    voice_input = voice.split()
    query = " ".join(str(que) for que in voice_input[1:len(voice_input)])
    url = "https://yandex.ru/search/?text=" + quote_plus(query)
    webbrowser.get().open(url)
    return voice


def open_users(voice: str):
    webbrowser.open('file:///Users/')
    return voice


def close(*args):
    sys.exit


def turn_on_audio(voice: str):
    osascript.osascript("set volume output volume 50")
    return voice


def turn_off_audio(voice: str):
    osascript.osascript("set volume output volume 0")
    return voice


def dot(voice: str):
    voice_input = voice.split()
    numbers = []
    for i in voice_input:
        if i.isnumeric() == True:
            numbers.append(int(i))

    if numbers[1] == 0:
        ans = voice + 'На 0 делить нельзя'
    else:
        ans = voice + '\nОтвет: '+ str(numbers[0] / numbers[1])
    return ans
