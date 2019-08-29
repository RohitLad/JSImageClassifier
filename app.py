from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/sample')
def running():
    return 'Flask is running!'

@app.route('/')
def predict():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()