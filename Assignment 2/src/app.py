from flask import Flask
from flask_cors import CORS  # Import CORS
from database import init_db
from task_manager import task_routes

app = Flask(__name__)

# Enable CORS
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

# Initialize database
init_db()

# Register blueprints
app.register_blueprint(task_routes)

if __name__ == "__main__": 
    app.run(debug=True)
