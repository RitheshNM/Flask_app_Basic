from types import MethodType
from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')

def home():
    return 'This is home page'

@app.route('/form')

def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])

def submit():
    return render_template('form.html')

@app.route('/heading')

def heading():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug= True)