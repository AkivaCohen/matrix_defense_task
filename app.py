from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def ping_service():
    return 'Hello, I am ping service!'

@app.route('/ping', methods = ['GET', 'POST'])
def do_ping():

    if request.method == 'GET':
        return 'GET method is not supported for this route, use POST.'

    if request.method == 'POST':
        return 'Pong'

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
