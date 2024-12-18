''' Creating a database and filling it out of CSV file '''
import csv
import sqlite3

# Function to read data from CSV file
def read_csv(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

# Function to create a SQLite database and table
def create_database(db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        name TEXT,
        height INTEGER,
        weight INTEGER,
        base_experience INTEGER,
        types TEXT,
        abilities TEXT
    )
    """)
    
    conn.commit()
    return conn, cursor

# Function to insert data into the database
def insert_data(cursor, table_name, data):
    for row in data:
        cursor.execute(f"""
        INSERT INTO {table_name} (name, height, weight, base_experience, types, abilities)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (row['name'], row['height'], row['weight'], row['base_experience'], row['types'], row['abilities']))
        
    cursor.connection.commit()

if __name__ == "__main__":
    # Define CSV filename and database parameters
    csv_filename = "pokemon_data.csv"
    db_name = "pokemon_data.db"
    table_name = "pokemon"
    
    # Read data from CSV
    csv_data = read_csv(csv_filename)
    
    if csv_data:
        # Create database and table
        conn, cursor = create_database(db_name, table_name)
        
        # Insert data into the database
        insert_data(cursor, table_name, csv_data)
        
        # Close the connection
        conn.close()
        
        print(f"Data successfully inserted into {db_name} database.")
    else:
        print("No data found in the CSV file.")
