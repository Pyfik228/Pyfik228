from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/')


@app.route('/')
def index ('/'):
    return render_template()






@app.route('/error')
def error():
    return "jkjkjk", 418

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
