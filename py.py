from flask import Flask, render_template, request, redirect, url_for
import ctypes

dll=ctypes.CDLL("C:\programing\site\my\dll.dll")

dll.ces.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_bool]
dll.ces.restype = ctypes.c_char_p

#a=input("text").encode("utf-8")
#b=input("key").encode("utf-8")
#c = bool(int(input("crypt?")))
#print(cesp.ces(a, b, c).decode())

app = Flask(__name__)

mode=True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ces', methods=["GET", "POST"])
def ces():
    global mode
    out = ""
    if request.method == "POST":
        if "toggle" in request.form:
            mode = not mode
        elif "proceed" in request.form:
            text = request.form.get("text", "").encode("utf-8")
            key = request.form.get("key", "").encode("utf-8")
            if text and key:
                res = dll.ces(text, key, mode)
                out = res.decode("utf-8")
        else: return redirect(url_for('index'))
    return render_template("ces.html", output=out, mod=mode)

@app.route('/about')
def about(): return render_template('about.html')

if __name__ == '__main__':
    app.run()