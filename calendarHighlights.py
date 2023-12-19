import sqlite3

def calendarHighlights():
    database_path = "job_application_tracker.db"
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute('SELECT Date_of_apply FROM Applications')
    results = cursor.fetchall()
    
    conn.close
    return results