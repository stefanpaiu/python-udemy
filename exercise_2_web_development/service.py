from flask import Flask
# Create a new Flask app by creating a new instance of Flask
app = Flask(__name__)
# Run the Flask using FLASK_APP=class_name.py flask run

@app.route("/")
def hello():
        return "Hello World!"

# This is a user as a parameter (the one in brackets)
@app.route("/user/<username>")
def show_user(username):
        return "User: %s" % username
