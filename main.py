from flask import Flask, render_template
import ctypes


cesp=ctypes.CDLL("cesp.dll")

cesp.ces.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_bool]
cesp.ces.restype = ctypes.c_char_p

a=input("text").encode("utf-8")
b=input("key").encode("utf-8")
c = bool.input("crypt?")
print(cesp.ces(a, b, c).decode())

#app = Flask(__name__)

#@app.route('/')
#def index():
#    return render_template('index.html')

#@app.route('/ces')
#def ces():
#    return render_template('ces.html')

#if __name__ == '__main__':
#    app.run()