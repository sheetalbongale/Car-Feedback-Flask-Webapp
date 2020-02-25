from flask import Flask, render_template, request

# initialize the app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True  # allows server to keep reloading
    app.run()