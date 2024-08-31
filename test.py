import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # replace with your MySQL username
        password="asd456asd456",  # replace with your MySQL password
        database="baby_surrogate"
    )
    return conn

def insert_full_data():
    # Full Test Data
    country = "USA"
    parent1_firstname = "John"
    parent1_lastname = "Doe"
    parent1_gender = "Male"
    parent1_citizenship = "American"
    parent1_birthdate = "1980-01-01"
    parent2_firstname = "Jane"
    parent2_lastname = "Doe"
    parent2_gender = "Female"
    parent2_citizenship = "American"
    parent2_birthdate = "1982-02-02"
    marriage_details = "Married"
    phone = "1234567890"
    email = "johndoe@example.com"
    address = "123 Main St, Anytown, USA"

    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert basic data first
    cursor.execute("""
        INSERT INTO parents (country, parent1_firstname, parent1_lastname, parent1_gender, parent1_citizenship, parent1_birthdate)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (country, parent1_firstname, parent1_lastname, parent1_gender, parent1_citizenship, parent1_birthdate))
    
    parent_id = cursor.lastrowid  # Get the last inserted ID
    
    # Update the remaining columns
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
    
    print("Full data inserted successfully with two steps!")

if __name__ == "__main__":
    insert_full_data()
