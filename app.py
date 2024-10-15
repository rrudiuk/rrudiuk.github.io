from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/data')
def get_data():
    data = {
        "Version_int": 3.8,
        "Version": "3.8"
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()
