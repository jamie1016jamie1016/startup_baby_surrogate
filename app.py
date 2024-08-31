from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/parent', methods=['GET', 'POST'])
def parent():
    return render_template('parent.html')

@app.route('/surrogate', methods=['GET', 'POST'])
def surrogate():
    return render_template('surrogate.html')

if __name__ == '__main__':
    app.run(debug=True)
