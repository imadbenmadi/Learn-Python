
import sqlite3

# 1. Connect to the SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('employee.db')

# 2. Create a cursor object
cursor = conn.cursor()

# 3. Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT,
    salary REAL
)
''')

# 4. Insert some data into the table
cursor.execute('INSERT INTO employees(name, department, salary) VALUES (?, ?, ?)', ('Alice', 'Sales', 40000))
cursor.execute('INSERT INTO employees(name, department, salary) VALUES (?, ?, ?)', ('Bob', 'HR', 40000))

# 5. Commit the transaction
conn.commit()

# 6. Execute a query to fetch data
cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()
for row in rows:
    print(row)

# 7. Execute a query to fetch specific data
cursor.execute('SELECT * FROM employees WHERE id = ?', (1,))
row = cursor.fetchone()
print(row)

# 8. Delete specific user
cursor.execute('DELETE FROM employees WHERE department = ?', ('Sales',))

# 9. Update user salary
cursor.execute('UPDATE employees SET salary = 55000 WHERE name = ?', ('John Doe',))

# 10. Commit changes
conn.commit()

# 11. Close the cursor and connection
cursor.close()
conn.close()