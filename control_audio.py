import socket
from subprocess import call

from flask import Flask, render_template, request


class SoundController:
    def __init__(self):
        self.html_path = None
        self.app = Flask(__name__)

        @self.app.route('/')
        def run():
            return render_template('index.html')

        @self.app.route("/vol_up/")
        def vol_up():
            print("VOLUME UP...!!!")
            call('nircmd.exe changesysvolume 1310', shell=True)
            return ""

        @self.app.route("/vol_down/")
        def vol_down():
            print("VOLUME DOWN...!!!")
            call('nircmd.exe changesysvolume -1310', shell=True)
            return ""

        @self.app.route("/space/")
        def space():
            print("SPACE...!!!")
            call('nircmd.exe sendkey spc press', shell=True)
            return ""

        @self.app.route("/left/")
        def left():
            print("LEFT...!!!")
            call('nircmd.exe sendkey left press', shell=True)
            return ""

        @self.app.route("/right/")
        def right():
            print("RIGHT...!!!")
            call('nircmd.exe sendkey right press', shell=True)
            return ""

        @self.app.route('/set_custom_vol', methods=['POST'])
        def set_vol():
            vol_value = request.form['vol_value']
            call('setvol {}'.format(vol_value), shell=True)
            return ""


if __name__ == '__main__':
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    SoundController().app.run(host=ip_addr, port=9001, debug=True)
