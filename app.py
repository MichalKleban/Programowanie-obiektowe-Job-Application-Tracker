from flask import Flask, render_template, redirect, request
from import_data import Import_data

app = Flask(__name__)

@app.route('/')
def home():
<<<<<<< HEAD
    query = Import_data.get_applications()
    return render_template('index.html.jinja', query=query)
=======
    calendarHighlights = Import_data.calendarHighlights()
    return render_template('index.html.jinja', calendarHighlights=calendarHighlights)
>>>>>>> 2a3ee915310387dca082f736a03c010892866cff
   
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