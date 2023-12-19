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
            company_name = request.form['company_name']
            position = request.form['position']
            date_of_apply = request.form['date_of_apply']
            side = request.form['side']
            status = request.form['status']
            cv_version = request.form['cv_version']
            mode = request.form['mode']
            contract_type = request.form['contract_type']
            job_type = request.form['job_type']
            application_data = Import_data(company_name, position, date_of_apply, side, status, cv_version, mode, contract_type, job_type)

        return application_data  

class Database:
    def __init__(self):
        pass     
    
    conn = sqlite3.connect('job_application_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Applications (
            id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
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
    data = (Import_data.received_data())
    cursor.execute(f'''
            INSERT INTO Applications (
                id, {data.company_name}, {data.position}, 
                {data.date_of_apply}, {data.side}, {data.status}, {data.cv_version}, {data.mode},
                {data.contract_type}, {data.job_type}) 
    ''')
    conn.commit()
    conn.close()