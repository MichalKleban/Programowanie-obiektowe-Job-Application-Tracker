from flask import Flask, render_template, redirect, request
from import_data import Import_data

app = Flask(__name__)

@app.route('/')
def home():
    calendarHighlights = Import_data.calendarHighlights()
    return render_template('index.html.jinja', calendarHighlights=calendarHighlights)
   
@app.route('/add_job', methods=['GET','POST'])
def add_job():
    if request.method == "POST":
        Import_data.insert_into_database()
        return redirect('/')
    else:
        err = "Oops... something went wrong"
        return render_template('index.html.jinja',err=err)


if __name__ == '__main__':
   app.run(debug=True)