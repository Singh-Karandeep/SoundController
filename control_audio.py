import socket
import time

import win32api
import win32con
from flask import Flask, render_template


class Event:
    KEY_REVERSE = 0x25
    KEY_FORWARD = 0x27
    KEY_VOL_UP = 0xAF
    KEY_VOL_DOWN = 0xAE
    KEY_PLAY_PAUSE = 0xB3
    KEY_NEXT_TRACK = 0xB0
    KEY_PREVIOUS_TRACK = 0xB1

    @staticmethod
    def press(code):
        win32api.keybd_event(code, 0, 0, 0)
        time.sleep(0.2)
        win32api.keybd_event(code, 0, win32con.KEYEVENTF_KEYUP, 0)


app = Flask(__name__)
event_obj = Event()


@app.route('/')
def run():
    return render_template('index.html')


@app.route("/vol_up/")
def vol_up():
    print("VOLUME UP...!!!")
    event_obj.press(Event.KEY_VOL_UP)
    return ""


@app.route("/vol_down/")
def vol_down():
    print("VOLUME DOWN...!!!")
    event_obj.press(Event.KEY_VOL_DOWN)
    return ""


@app.route("/play_pause/")
def play_pause():
    print("PLAY/PAUSE...!!!")
    event_obj.press(Event.KEY_PLAY_PAUSE)
    return ""


@app.route("/reverse/")
def reverse():
    print("REVERSE...!!!")
    event_obj.press(Event.KEY_REVERSE)
    return ""


@app.route("/forward/")
def forward():
    print("FORWARD...!!!")
    event_obj.press(Event.KEY_FORWARD)
    return ""


@app.route("/previous_track/")
def previous_track():
    print("PREVIOUS TRACK...!!!")
    event_obj.press(Event.KEY_PREVIOUS_TRACK)
    return ""


@app.route("/next_track/")
def next_track():
    print("NEXT TRACK...!!!")
    event_obj.press(Event.KEY_NEXT_TRACK)
    return ""


if __name__ == '__main__':
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    app.run(host=ip_addr, port=9001, debug=True)
