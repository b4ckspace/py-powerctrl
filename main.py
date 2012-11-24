from flask import Flask, request, render_template, redirect, url_for
from powerctrl import Powerctrl

app = Flask(__name__)
pwctrl = Powerctrl('/dev/ttyUSB0')

@app.route("/")
def page_index():
    return render_template('index.html')

@app.route("/relais")
def page_cmd():

    relais = request.values.get('relais')
    value = request.values.get('value')

    pwctrl.port_set( int(relais), int(value) )

    return redirect(url_for('page_index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
