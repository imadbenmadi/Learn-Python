from flask import Flask
from database import init_db
from task_manager import task_routes
app = Flask(__name__)

# Initialize database
init_db()

# Instead of defining all routes in the main app file, we can create separate blueprints and register them with the main app.
app.register_blueprint(task_routes)

if __name__ == "__main__": 
    app.run(debug=True)
