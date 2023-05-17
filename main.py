from flask import *
import search

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("run.html")

@app.route('/success', methods=['POST'])
def success():
    try:
        if request.method == 'POST':
            word = ''
            f = request.files['file']
            f.save(f.filename)
            print(f.filename)
            word = search.Search(f.filename)
            return render_template("success.html", word=word)
    except:
        return render_template("run.html")

@app.route("/success", methods=["POST"])
def move_forward():
    return render_template("run.html")

if __name__ == '__main__':
    app.run(debug=True)