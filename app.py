# app.py

# Import the necessary Flask components
from flask import Flask

# Create an instance of the Flask class
# This makes 'app' the central object for the web application
app = Flask(__name__)

# --- Route Definitions ---

# Define the default route (the home page: http://localhost:8080/)
@app.route('/')
def home():
    # Return the HTML content to be displayed in the browser
    return "<h1>Hello, Python Web App!</h1><p>This page is running from a Docker container.</p>"

# Define a second route (the about page: http://localhost:8080/about)
@app.route('/about')
def about():
    # Return different content for this route
    return "<h2>About This App</h2><p>This simple application demonstrates how to containerize a Flask app.</p>"

# The following block is typically used to run the app locally,
# but when using Docker's 'flask run --host=0.0.0.0' command, it's optional.
# We include it here for completeness and easy local testing outside of Docker.
if __name__ == '__main__':
    # 'host=0.0.0.0' makes the server externally accessible within the container network
    # 'debug=True' enables the reloader and debugger
    app.run(debug=True, host='0.0.0.0', port=8080)