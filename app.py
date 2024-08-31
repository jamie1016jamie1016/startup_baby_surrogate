from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL configurations
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # replace with your MySQL username
        password="asd456asd456",  # replace with your MySQL password
        database="baby_surrogate"
    )
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/parent', methods=['GET', 'POST'])
def parent():
    if request.method == 'POST':
        details = request.form
        country = details['country']
        parent1_firstname = details['parent1-firstname']
        parent1_lastname = details['parent1-lastname']
        parent1_gender = details['parent1-gender']
        parent1_citizenship = details['parent1-citizenship']
        parent1_birthdate = details['parent1-birthdate']
        parent2_firstname = details['parent2-firstname']
        parent2_lastname = details['parent2-lastname']
        parent2_gender = details['parent2-gender']
        parent2_citizenship = details['parent2-citizenship']
        parent2_birthdate = details['parent2-birthdate']
        marriage_details = details['marriage-details']
        phone = details['phone']
        email = details['email']
        address = details['address']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Step 1: Insert basic data
        cursor.execute("""
            INSERT INTO parents(country, parent1_firstname, parent1_lastname, parent1_gender, parent1_citizenship, parent1_birthdate)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (country, parent1_firstname, parent1_lastname, parent1_gender, parent1_citizenship, parent1_birthdate))
        
        parent_id = cursor.lastrowid  # Get the last inserted ID
        
        # Step 2: Update remaining columns
        cursor.execute("""
            UPDATE parents SET
            parent2_firstname = %s,
            parent2_lastname = %s,
            parent2_gender = %s,
            parent2_citizenship = %s,
            parent2_birthdate = %s,
            marriage_details = %s,
            phone = %s,
            email = %s,
            address = %s
            WHERE id = %s
        """, (parent2_firstname, parent2_lastname, parent2_gender, parent2_citizenship, parent2_birthdate,
              marriage_details, phone, email, address, parent_id))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return 'Parent Information Submitted Successfully!'
    
    return render_template('parent.html')

@app.route('/surrogate', methods=['GET', 'POST'])
def surrogate():
    if request.method == 'POST':
        details = request.form
        name = details['surrogate-name']
        email = details['surrogate-email']
        phone = details['surrogate-phone']
        address = details['surrogate-address']
        profession = details['surrogate-profession']
        reason_surrogate = details['reason-surrogate']
        height = float(details['height'])
        weight = float(details['weight'])
        medical_history = details['medical-history']
        age = int(details['age'])
        surrogate_before = details['surrogate-before']
        surrogate_times = int(details.get('surrogate-times', 0))
        mother = int(details.get('mother', 0))
        criminal_record = details['criminal-record']
        criminal_details = details.get('criminal-details-text', '')
        additional_info = details.get('additional-info', '')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Step 1: Insert basic data
        cursor.execute("""
            INSERT INTO surrogates(name, email, phone, address, profession, reason_surrogate)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (name, email, phone, address, profession, reason_surrogate))
        
        surrogate_id = cursor.lastrowid  # Get the last inserted ID
        
        # Step 2: Update remaining columns
        cursor.execute("""
            UPDATE surrogates SET
            height = %s,
            weight = %s,
            medical_history = %s,
            age = %s,
            surrogate_before = %s,
            surrogate_times = %s,
            mother = %s,
            criminal_record = %s,
            criminal_details = %s,
            additional_info = %s
            WHERE id = %s
        """, (height, weight, medical_history, age, surrogate_before, surrogate_times, mother,
              criminal_record, criminal_details, additional_info, surrogate_id))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return 'Surrogate Information Submitted Successfully!'
    
    return render_template('surrogate.html')

if __name__ == '__main__':
    app.run(debug=True)
