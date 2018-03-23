from flask import Flask, render_template, make_response
from brd import black_region_detection

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/html')
def html():
    return render_template('hello.html')

@app.route('/chart/<pair>')
def chart(pair):
    return render_template('chart.html', pair = pair)

@app.route("/brd/<num>")
def brd(num):
    return render_template('brd/brd.html', black_regions = black_region_detection.detect(num))



@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


if __name__ == '__main__':
  app.run(debug=True)
