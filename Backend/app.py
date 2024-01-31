from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# Database connection
db_params = {
    'dbname': 'thwekqkk',
    'user': 'thwekqkk',
    'password': 'wo5PkAQTCUFiks0wZ9EvnlrSasp0O1g0',
    'host': 'dumbo.db.elephantsql.com',
    'port': '5432',
}

def connect_to_db():
    try:
        connection = psycopg2.connect(**db_params)
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def query_database():
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users;")
        data = cursor.fetchall()
        connection.close()
        return data
    else:
        return []

def insert_user(name):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (%s);", (name,))
        connection.commit()
        connection.close()
        return True
    else:
        return False

def delete_user(name):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM users WHERE name = %s;", (name,))
        connection.commit()
        connection.close()
        return True
    else:
        return False

@app.route('/api/data', methods=['GET'])
def get_data():
    data = query_database()
    return jsonify({'data': data})

@app.route('/api/insert', methods=['POST'])
def insert_data():
    data = request.get_json()
    name = data.get('name')
    
    if insert_user(name):
        return jsonify({'message': 'User inserted successfully!'}), 200
    else:
        return jsonify({'message': 'Failed to insert user.'}), 500

@app.route('/api/delete', methods=['POST'])
def delete_data():
    data = request.get_json()
    name = data.get('name')
    
    if delete_user(name):
        return jsonify({'message': 'User deleted successfully!'}), 200
    else:
        return jsonify({'message': 'Failed to delete user.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
