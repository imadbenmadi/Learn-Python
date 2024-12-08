import sqlite3
from flask import Flask, jsonify, request, render_template

# Create Flask Application Instance
app = Flask(__name__)


# a. Get All Employees
@app.route('/employees', methods=["GET"])
def get_data():
    # Connect to SQLite database
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()

    # Execute query to fetch all employees
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    # Close the connection
    cursor.close()
    conn.close()

    # Convert query result to a list of dictionaries
    user_list = [{"id": user[0], "name": user[1], "dep": user[2], "sal": user[3]} for user in rows]
    return jsonify(user_list)  # Return the list of users as JSON

# b. Get Employee by ID
@app.route('/employees/<int:id>', methods=["GET"])
def get_data_id(id):
    # Connect to SQLite database
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()

    # Execute query to fetch employee by ID
    cursor.execute("SELECT * FROM employees WHERE id = ?", (id,))
    row = cursor.fetchone()

    # Close the connection
    cursor.close()
    conn.close()

    # Return user data or an error message if the user is not found
    if row is None:
        return "User not found!", 404
    else:
        return jsonify({"id": row[0], "name": row[1], "dep": row[2], "sal": row[3]})

# c. Add a New Employee
@app.route('/employees/new', methods=["POST"])
def put_data():
    # Get new user data from the JSON request body
    new_user = request.json
    
    # Connect to SQLite database
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()

    # Execute SQL to insert a new employee record
    cursor.execute('INSERT INTO employees(name, department, salary) VALUES (?, ?, ?)', 
                   (new_user["name"], new_user["department"], new_user["salary"]))
    
    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()

    # Return a success message
    return "New user created", 201
@app.route('/employees/update/<int:id>', methods=["PUT"])
def update_data(id):
    # Get new user data from the JSON request body
    new_user = request.json
    
    # Connect to SQLite database
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()

    # Execute SQL to insert a new employee record
    cursor.execute('UPDATE employees SET name = ?, department = ?, salary = ? WHERE id = ?', 
                   (new_user["name"], new_user["department"], new_user["salary"], id))
    
    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()

    # Return a success message
    return "User updated", 201
@app.route('/employees/delete/<int:id>', methods=["DELETE"])
def delete_data(id):
    # Connect to SQLite database
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()

    # Execute SQL to insert a new employee record
    cursor.execute('DELETE FROM employees WHERE id = ?', (id,))
    
    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()

    # Return a success message
    return "User deleted", 201

# Run the Flask Application
if __name__ == '__main__':
    app.run(debug=True, port=5015)
