from flask import Flask, render_template, request, redirect, url_for
import ctypes, os, platform
from os import getenv

if platform.system() == "Windows":
    dll = ctypes.CDLL(os.path.abspath("dll.dll"))
else:
    dll = ctypes.CDLL(os.path.abspath("cesp.so"))

dll.mix.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_bool]
dll.mix.restype = ctypes.c_char_p

dll.ces.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_bool]
dll.ces.restype = ctypes.c_char_p

app = Flask(__name__)

mode=True

@app.route('/')
def index():
    return render_template('index.html')

fun=[dll.ces, dll.mix]
nms=["ces", "mix"]
lks=["{{ url_for('ces') }}", "{{ url_for('mix') }}"]
def crypt(n):
    global mode
    out = ""
    if request.method == "POST":
        if "toggle" in request.form:
            mode = not mode
        elif "proceed" in request.form:
            text = request.form.get("text", "").encode("utf-8")
            key = request.form.get("key", "").encode("utf-8")
            if text and key:
                res = fun[n](text, key, mode)
                out = res.decode("utf-8")
        else: return redirect(url_for('index'))
    return render_template("tool.html", output=out, mod=mode, title=nms[n], links=lks[n])

@app.route('/ces', methods=["GET", "POST"])
def ces(): return crypt(0)

@app.route('/mix', methods=["GET", "POST"])
def mix(): return crypt(1)


@app.route('/menu')
def menu(): return render_template('menu.html')

@app.route('/about')
def about(): return render_template('about.html')

if __name__ == '__main__':
    if platform.system() == "Windows":
        app.run()
    else:
        port = int(getenv("PORT", 10000))
        app.run(host='0.0.0.0', port=port)