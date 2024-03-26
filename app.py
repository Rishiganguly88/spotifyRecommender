from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

# Database connection parameters
host = ''
user = ''
password = ''
database = ''

# Function to insert data into the database
def insert_data(name, age, email, options):
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=database,
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO your_table_name (name, age, email, options) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (name, age, email, options))
            connection.commit()
    finally:
        connection.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        options = ', '.join(request.form.getlist('options'))  # Combine selected options into a string

        # Insert data into the database
        insert_data(name, age, email, options)
        
        return 'Form submitted successfully!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
