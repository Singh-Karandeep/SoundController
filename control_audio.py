import socket
import subprocess
from os import getcwd
from flask import Flask, render_template, request

app = Flask(__name__, template_folder=getcwd())


@app.route('/')
def run():
    return render_template('index.html')


@app.route("/vol_up/")
def vol_up():
    print("VOLUME UP...!!!")
    subprocess.call('nircmd.exe changesysvolume 1310', shell=True)
    return ""


@app.route("/vol_down/")
def vol_down():
    print("VOLUME DOWN...!!!")
    subprocess.call('nircmd.exe changesysvolume -1310', shell=True)
    return ""


@app.route("/space/")
def space():
    print("SPACE...!!!")
    subprocess.call('nircmd.exe sendkey spc press', shell=True)
    return ""


@app.route("/left/")
def left():
    print("LEFT...!!!")
    subprocess.call('nircmd.exe sendkey left press', shell=True)
    return ""


@app.route("/right/")
def right():
    print("RIGHT...!!!")
    subprocess.call('nircmd.exe sendkey right press', shell=True)
    return ""


@app.route('/set_custom_vol', methods=['POST'])
def set_vol():
    vol_value = request.form['vol_value']
    subprocess.call('setvol {}'.format(vol_value), shell=True)
    return ""


if __name__ == '__main__':
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    app.run(host=ip_addr, port=9001, debug=True)
