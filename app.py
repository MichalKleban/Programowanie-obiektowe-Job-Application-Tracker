import sqlite3
from flask import Flask, render_template, redirect, request
from import_data import Import_data
import calendarHighlights

app = Flask(__name__)

@app.route('/')
def home():

    query = Import_data.get_applications()
    specjalDays = calendarHighlights.calendarHighlights()
    return render_template('index.html.jinja', daysToHighlight=specjalDays, query=query)

@app.route('/add_job', methods=['GET','POST'])
def add_job():
    if request.method == "POST":
        Import_data.insert_into_database()
        return redirect('/')
    else:
        err = "Oops... something went wrong"
        return render_template('index.html.jinja',err=err)
    
@app.route('/edit_job', methods=['GET','POST'])
def edit_job():
    if request.method == "POST":
        Import_data.update_database()
        return redirect('/')
    else:
        err = "Oops... something went wrong"
        return render_template('index.html.jinja',err=err)

if __name__ == '__main__':
   app.run(debug=True)