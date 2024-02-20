# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for

# Initialize Flask application
app = Flask(__name__)

# Define routes
#Jonah is the best programmer
#jonah is not the best
@app.route('/')
def index():
    a = 1
    print(a)
    return render_template('index.html')

# Define routes
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle signup form submission
        # Extract form data and store in the database
        name = request.form["name"]
        email = request.form["email"]
        print(name, email)
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle signup form submission
        # Extract form data and store in the database
        name = request.form["name"]
        pass
    return render_template('signup.html')

@app.route('/challenge', methods=['GET', 'POST'])
def challenge():
    if request.method == 'POST':
        # Handle challenge submission
        # Validate the challenge and process it
        pass
    return render_template('challenge.html')

# Add more routes as needed

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
