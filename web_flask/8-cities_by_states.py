#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def state():
    state = storage.all("State").values()
    return render_template("7-states_list.html", state=state)


@app.route('/cities_by_states')
def state_cities():
    state = storage.all("State")
    return render_template('8-cities_by_states.html', state=state)


@app.teardown_appcontext
def close_session(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
