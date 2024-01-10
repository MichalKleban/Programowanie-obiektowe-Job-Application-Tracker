import sqlite3
from flask import Flask, request
app = Flask(__name__)

class Import_data:
    def __init__(self, company_name, position, date_of_apply, site, status, cv_version, mode, contract_type, job_level):
        self.company_name = company_name
        self.position = position
        self.date_of_apply = date_of_apply
        self.site = site
        self.status = status
        self.cv_version = cv_version
        self.mode = mode
        self.contract_type = contract_type
        self.job_level = job_level
        
    @app.route('/', methods=['POST', 'GET'])
    def received_data():
        
        company_name = request.form['company_name']
        position = request.form['position']
        date_of_apply = request.form['date_of_apply']
        site = request.form['site']
        status = request.form['status']
        cv_version = request.form['cv_version']
        mode = request.form['mode']
        contract_type = request.form['contract_type']
        job_level = request.form['job_level']
        application_data = Import_data(company_name, position, date_of_apply, site, status, cv_version, mode, contract_type, job_level)

        return application_data  
    
    def insert_into_database():
            
        conn = sqlite3.connect('job_application_tracker.db')
        cursor = conn.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS Applications (
                    Id INTEGER PRIMARY KEY,
                    Company_name TEXT,
                    Position TEXT,
                    Date_of_apply DATE,
                    Site TEXT,
                    Status TEXT,
                    Cv_version TEXT,
                    Mode TEXT,
                    Contract_type TEXT, 
                    job_level TEXT
                )
            ''')
        data = Import_data.received_data()
        cursor.execute('''
                INSERT INTO Applications (
                    Company_name, Position, Date_of_apply, Site, 
                    Status, Cv_version, Mode, Contract_type, job_level
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ? )''',(data.company_name, data.position, data.date_of_apply, data.site, data.status, data.cv_version, data.mode, data.contract_type, data.job_level))
        conn.commit()
        conn.close()

    def get_applications():
        database_path = "job_application_tracker.db"
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Applications')
        results = cursor.fetchall()
        
        conn.close
        return results
        
        

