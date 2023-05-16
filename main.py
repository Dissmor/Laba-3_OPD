from distutils.log import debug
from fileinput import filename
from flask import *
import search

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("run.html")


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        word = ''
        f = request.files['file']
        f.save(f.filename)
        word = search.Search()
        return render_template("success.html", word=word)


if __name__ == '__main__':
    app.run(debug=True)