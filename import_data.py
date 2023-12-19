import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)

class Import_data:
    def __init__(self, company_name, position, date_of_apply, side, status, cv_version, mode, contract_type, job_type):
        self.company_name = company_name
        self.position = position
        self.date_of_apply = date_of_apply
        self.side = side
        self.status = status
        self.cv_version = cv_version
        self.mode = mode
        self.contract_type = contract_type
        self.job_type = job_type

    @app.route('/', methods= ['GET', 'POST'])
    
    def received_data():
        if request.method == 'POST':
            id = 1
            company_name = request.form['company_name']
            position = request.form['position']
            date_of_apply = request.form['date_of_apply']
            side = request.form['side']
            status = request.form['status']
            cv_version = request.form['cv_version']
            mode = request.form['mode']
            contract_type = request.form['contract_type']
            job_type = request.form['job_type']
            application_data = Import_data(id, company_name, position, date_of_apply, side, status, cv_version, mode, contract_type, job_type)

        return application_data  
    if __name__ == '__main__':
        app.run(debug=True)
class Database:
    def __init__(self):
        pass     
    
    conn = sqlite3.connect('job_application_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Applications (
            id INTEGER PRIMARY KEY,
            company_name TEXT,
            position TEXT,
            date_of_apply DATE,
            side TEXT,
            status TEXT,
            cv_version TEXT,
            mode TEXT,
            contract_type TEXT, 
            job_type TEXT
        )
    ''')
    date = (Import_data.received_data())
    cursor.execute('''
            INSERT INTO Applications (
                id, company_name, position, 
                date_of_apply, side, status, cv_version, mode,
                contract_type, job_type) 
    ''')
    conn.commit()
    conn.close()