from flask import Flask, render_template, request, Response
import time
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/stream')
def run():
    def getdata():
        num=0
        while True:
            num=num+10
            time.sleep(1)
            yield "\nNumber is: " + str(num)
    return Response(getdata(), mimetype= 'text/event-stream')
if __name__ == "__main__":
    app.debug = True
    app.run(threaded=True)
