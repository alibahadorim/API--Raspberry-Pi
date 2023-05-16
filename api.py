
from flask import Flask, jsonify, abort, request, make_response, url_for
from sense_hat import SenseHat

# initialize variables
r = 255
g = 255
b = 255

def set_leds(r, g, b):
    sense = SenseHat()
    c = [r, 0, 0] # color
    b = [0, 0, 0] # background color
    shape = [
    b, b, b, b, b, b, b, b,
    b, c, b, b, b, c, b, b,
    c, c, c, b, c, c, c, b,
    c, c, c, c, c, c, c, c,
    b, c, c, c, c, c, c, b,
    b, b, c, c, c, c, b, b,
    b, b, b, c, c, b, b, b,
    b, b, b, b, b, b, b, b
]

    sense.set_pixels(shape)

def reset_colors():
    sense = SenseHat()
    sense.clear()

app = Flask(__name__, static_url_path="")

# error handlers
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

# POST request
@app.route('/assignment5/sensor', methods=['POST'])
def get_sensor_data():
    sense = SenseHat()
    temperature = round(sense.get_temperature(), 2)
    humidity = round(sense.get_humidity(), 2)
    pressure = round(sense.get_pressure(), 2)
    data = {'temperature': temperature, 'humidity': humidity, 'pressure': pressure}
    return jsonify(data), 200

# POST request
@app.route('/assignment5/actuator/led', methods=['POST'])
def set_led():
    status = "off"
    if not request.json or not 'toggle' in request.json:
        abort(400)

    if request.json['toggle'] > 0:
        red = request.json['red']
        blue = request.json['blue']
        print(str(red))
        print(str(blue))
        set_leds(red, g, blue)
        status = "on"
    else:
        reset_colors()
        status = "off"

    return jsonify({'status': status}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)

