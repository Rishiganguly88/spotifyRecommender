from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

# Database connection parameters
host = ''
user = ''
password = ''
database = ''

# Function to insert data into the database
def insert_data(name, email, age, genres):
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=database,
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO your_table_name (name, email, age, genres) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (name, email, age, genres))
            connection.commit()
    finally:
        connection.close()

@app.route('/submit', methods=['POST'])
def submit_form():
    # Retrieve form data
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    genres = request.form['selectedGenres']

    # Insert data into the database
    insert_data(name, email, age, genres)
    
    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
