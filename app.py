from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/data')
def get_data():
    data = {
        "Version_int": 2,
        "Version": "2.0.1"
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()