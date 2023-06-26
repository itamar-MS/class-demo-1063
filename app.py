from flask import Flask, jsonify, render_template

app = Flask(__name__)

# In-memory data store
weather_data = [
    {'id': 1, 'city': 'San Francisco', 'temperature': 68, 'weather': 'Sunny'},
    {'id': 2, 'city': 'New York', 'temperature': 77, 'weather': 'Rainy'}
]

alerts_data = [
    {'id': 1, 'city': 'San Francisco', 'alert': 'Heat wave expected'},
    {'id': 2, 'city': 'New York', 'alert': 'Flash flood warning'}
]


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
