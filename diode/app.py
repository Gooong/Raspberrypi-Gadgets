from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

channel=12
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

# GPIO.cleanup()

@app.route('/')
def hello_world():
    return app.send_static_file('index.html')

@app.route('/on')
def turn_on():
    GPIO.output(channel, GPIO.HIGH)
    return "OK"

@app.route('/off')
def turn_off():
    GPIO.output(channel, GPIO.LOW)
    return "OK"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

