from flask import Flask, render_template
import myCalendar
app = Flask(__name__)

@app.route('/')
def home():
    calendar_template = myCalendar.showCalendar(2023, 5, [1,4])
    return render_template('index.html.jinja', calendar_template=calendar_template)

if __name__ == '__main__':
   app.run(debug=True)