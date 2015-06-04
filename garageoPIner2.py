from functools import wraps
from flask import session,request, Response, Flask
from threading import Timer
import RPi.GPIO as GPIO
import time
from datetime import timedelta
import configparser

app = Flask(__name__)
app.secret_key = 'm4bG3YJwarQQXU3T' #Needed for keep session open

GO_USERNAME = 'admin'
GO_PASSWORD = 'garageopiner'
GO_PORT = 80

GO_PIN1 = 4
GO_PIN2 = 17


GPIO.setmode(GPIO.BCM)

timer1 = None #Timer for Door1
timer2 = None # Timer for Door2


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == GO_USERNAME and password == GO_PASSWORD

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/toggleIN1')
@requires_auth
def toggleIN1():
    try:
        stopTimeControlIN1()
        togglePin(GO_PIN1)
        response = "Relay switched successfull."
    except Exception as e:
        response = "Error occured: " + str(e)
    return response

@app.route('/toggleIN2')
@requires_auth
def toggleIN2():
    try:
        stopTimeControlIN1()
        togglePin(GO_PIN2)
        response = "Relay switched successfull."
    except Exception as e:
        response = "Error occured: " + str(e)
    return response ;

@app.route('/timeControlIN1')
@requires_auth
def timeControlIN1():
    global timer1
    seconds = request.args.get('seconds')

    #Keep session open to allow timer to switch relay again
    session.permanent = True
    app.permanent_session_lifetime = timedelta(seconds=int(seconds)+5)

    stopTimeControlIN1()
    togglePin(GO_PIN1)
    timer1 = Timer(int(seconds),togglePin, [GO_PIN1])
    timer1.start()
    return "Timer started"

@app.route('/stopTimeControlIN1')
def stopTimeControlIN1():
    global timer1
    if timer1!=None:
        timer1.cancel()
        timer1=None
        return "Timer canceled"

@app.route('/timeControlIN2')
@requires_auth
def timeControlIN2():
    global timer2
    seconds = request.args.get('seconds')

    #Keep session open to allow timer to switch relay again
    session.permanent = True
    app.permanent_session_lifetime = timedelta(seconds=int(seconds)+5)

    stopTimeControlIN2()
    togglePin(GO_PIN2)
    timer2 = Timer(int(seconds),togglePin, [GO_PIN2])
    timer2.start()
    return "Timer started"

@app.route('/stopTimeControlIN2')
@requires_auth
def stopTimeControlIN2():
    global timer2
    if timer2!=None:
        timer2.cancel()
        timer2=None
        return "Timer canceled"

@app.route('/')
@requires_auth
def deliverWebPage():
    return app.send_static_file('index.html')

def togglePin(pin):
    GPIO.setup(int(pin), GPIO.OUT)
    GPIO.output(int(pin),GPIO.LOW)
    time.sleep(0.2);
    GPIO.output(int(pin),GPIO.HIGH)


if __name__ == '__main__':
    config = configparser.RawConfigParser()
    config.read('garageoPIner.cfg')

    GO_PORT = int(config.get("Settings","port"))
    GO_PIN1 = int(config.get("Settings","pin1"))
    GO_PIN2 = int(config.get("Settings","pin2"))

    GO_USERNAME = config.get("Credentials","username")
    GO_PASSWORD = config.get("Credentials","password")


    GPIO.setup(GO_PIN1,GPIO.IN)
    GPIO.setup(GO_PIN2,GPIO.IN)
    app.run(host='0.0.0.0',debug=True)
