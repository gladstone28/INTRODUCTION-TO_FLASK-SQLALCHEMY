from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Database configuration
app = Flask(__name__)  # Application instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'  # Path to database and its name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To suppress warning
db = SQLAlchemy(app)  # Database instance

# Routing for displaying the home page
@app.route('/')
@app.route('/home')
def home():
    return "Wow!!! Congrats! You have just created your first Flask application supporting databases!"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
