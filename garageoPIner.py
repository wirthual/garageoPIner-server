from functools import wraps
from flask import session,request, Response, Flask
from threading import Timer
import RPi.GPIO as GPIO
import time
from datetime import timedelta

app = Flask(__name__)

GO_USERNAME = 'admin'
GO_PASSWORD = 'garageopiner'


GPIO.setmode(GPIO.BCM)
t = None
app.secret_key = 'secret'

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

@app.route('/controlRelay/<pin>')
@requires_auth
def controlRelay(pin):
    try:
        switchPin(pin)
        response = "Relay switched successfull."
    except Exception as e:
        response = "Error occured: " + str(e)
    return response ;    

@app.route('/timeControl')
@requires_auth
def TimerStart():
    global t
    seconds = request.args.get('seconds')
    pin = request.args.get('pin')	

    #Keep session open to allow timer to switch relay again
    session.permanent = True
    app.permanent_session_lifetime = timedelta(seconds=int(seconds)+5)

    switchPin(pin)
    t = Timer(int(seconds),switchPin, pin)
    t.start()
    return "Timer started"

@app.route('/cancelTimer')
def TimerStop():
    global t
    if t!=None:
        t.cancel()
        t=None
        return "Timer canceled"

@app.route('/')
@requires_auth
def deliverWebPage():
    return app.send_static_file('index.html')

def switchPin(pin):
    TimerStop()
    GPIO.setup(int(pin), GPIO.OUT)
    GPIO.output(int(pin),GPIO.HIGH)
    time.sleep(0.2);
    GPIO.output(int(pin),GPIO.LOW)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
