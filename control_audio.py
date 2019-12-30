import socket
import time

import win32api
import win32con
from flask import Flask, render_template


class Event:
    # CODES : https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
    KEY_REVERSE = 0x25
    KEY_FORWARD = 0x27
    KEY_VOL_UP = 0xAF
    KEY_VOL_DOWN = 0xAE
    KEY_PLAY_PAUSE = 0xB3
    KEY_NEXT_TRACK = 0xB0
    KEY_PREVIOUS_TRACK = 0xB1
    KEY_YOUTUBE_PREVIOUS_TRACK = [0x10, 0x50]
    KEY_YOUTUBE_NEXT_TRACK = [0x10, 0x4E]

    @staticmethod
    def single_press(code):
        win32api.keybd_event(code, 0, 0, 0)
        time.sleep(0.2)
        win32api.keybd_event(code, 0, win32con.KEYEVENTF_KEYUP, 0)

    @staticmethod
    def combi_press(codes):
        for code in codes:
            win32api.keybd_event(code, 0, 0, 0)
            time.sleep(0.2)
        for code in codes[::-1]:
            win32api.keybd_event(code, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.1)


app = Flask(__name__)
event_obj = Event()


@app.route('/')
def run():
    return render_template('index.html')


@app.route("/vol_up/")
def vol_up():
    print("VOLUME UP...!!!")
    event_obj.single_press(Event.KEY_VOL_UP)
    return ""


@app.route("/vol_down/")
def vol_down():
    print("VOLUME DOWN...!!!")
    event_obj.single_press(Event.KEY_VOL_DOWN)
    return ""


@app.route("/play_pause/")
def play_pause():
    print("PLAY/PAUSE...!!!")
    event_obj.single_press(Event.KEY_PLAY_PAUSE)
    return ""


@app.route("/reverse/")
def reverse():
    print("REVERSE...!!!")
    event_obj.single_press(Event.KEY_REVERSE)
    return ""


@app.route("/forward/")
def forward():
    print("FORWARD...!!!")
    event_obj.single_press(Event.KEY_FORWARD)
    return ""


@app.route("/previous_track/")
def previous_track():
    print("PREVIOUS TRACK...!!!")
    event_obj.single_press(Event.KEY_PREVIOUS_TRACK)
    return ""


@app.route("/next_track/")
def next_track():
    print("NEXT TRACK...!!!")
    event_obj.single_press(Event.KEY_NEXT_TRACK)
    return ""


@app.route("/youtube_previous_track/")
def youtube_previous_track():
    print("YOUTUBE PREVIOUS TRACK...!!!")
    event_obj.combi_press(Event.KEY_YOUTUBE_PREVIOUS_TRACK)
    return ""


@app.route("/youtube_next_track/")
def youtube_next_track():
    print("YOUTUBE NEXT TRACK...!!!")
    event_obj.combi_press(Event.KEY_YOUTUBE_NEXT_TRACK)
    return ""


if __name__ == '__main__':
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    app.run(host=ip_addr, port=9001, debug=True)
