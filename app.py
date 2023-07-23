import os
from flask import Flask, request
import pymysql
import json


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#DB_NAME = "my_db"

def connection():
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="root@123",
        db="my_db",
        port=3306
    )
    return db

@app.route('/add_employee', methods=['POST'])
def add_employee():
    input_data = request.get_json()
    name = input_data.get('name')
    email = input_data.get('email')
    department = input_data.get('department')

    with connection() as db:
        cursor = db.cursor()
        query = "INSERT INTO employee (name, email, department) VALUES ('" + name + "', '" + email + "', '" + department + "')"
        cursor.execute(query)
        db.commit()
    return 'Employee added successfully!'

@app.route('/display', methods=['GET'])
def index():
    with connection() as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM employee")
        json_data = json.dumps([{
            'name': employee[0],
            'email': employee[1],
            'department': employee[2]
        } for employee in cursor])
    return json_data


if __name__ == '__main__':
    app.run()
