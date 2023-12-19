from flask import Flask, render_template
import import_data
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html.jinja')

if __name__ == '__main__':
   app.run(debug=True)