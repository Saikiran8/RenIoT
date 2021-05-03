from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hey Saiki"
@app.route('/saiki')
def pint():
    return "Hey Pintu"


if __name__ == '__main__':
    app.run(port=5000, debug=True)