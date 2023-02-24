import speech_recognition as sr
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import functions as f


# Список команд для ассистента
commands = {
    ('открыть диспетчер задач', 'открой диспетчер задач'): f.open_disp,
    ('открыть настройки', 'открой настройки'): f.open_settings,
    ('найди'): f.find_in_internet,
    ('закрыть ассистента'): f.close,
    ('открой папку пользователя', 'открыть папку пользователя'): f.open_users,
    ('выключи звук', 'выключить звук'): f.turn_off_audio,
    ('включи звук', 'включить звук'): f.turn_on_audio,
    ('подели', 'поделить'): f.dot
}


# Клас для оконного приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Голосовой ассистент")
        self.setGeometry(500, 400, 250, 300)

        self.button = QPushButton("?", self)
        self.button.resize(200, 150)
        self.button.move(25, 10)
        self.button.clicked.connect(self.cont)

        self.textLabel = QLabel("Ваша команда: \n", self)
        self.textLabel.move(25, 175)
        self.textLabel.resize(200, 50)

    def cont(self):
        voice_input = listen()
        self.textLabel.setText("Ваша команда: \n" + execute_command_with_name(voice_input))


def listen(*args):
    """
    Запись и распознавание аудио
    :return: распознанный голос
    """
    with sr.Microphone() as mic:
        out = ""

        recognizer.adjust_for_ambient_noise(mic, duration=1)

        try:
            audio = recognizer.listen(mic, 5, 5)

        except sr.WaitTimeoutError:
            out = "Ничего не услышал("
            return out

        try:
            out = recognizer.recognize_google(audio, language="ru").lower()

        except sr.UnknownValueError:
            pass

        return out


# Функция для определения сказанной команды
def execute_command_with_name(voice: str):
    """
    Выполнение команды, которая была в голосе
    :param voice: поданный голос
    :return:
    """
    try:
        first_word = voice.split()[0]
        for key in commands.keys():
            if voice in key or first_word in key:
                return commands[key](voice)
            else:
                pass
        return voice + '\nКоманда не распознанна('

    except:
        return 'Ничего не услышал('


if __name__ == "__main__":

    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 0.5

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()