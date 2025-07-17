# filepath: c:\Users\attap\Documents\Portfolio\portfolio-template\app.py
from flask import Flask, render_template

print("Starting the app...")
app = Flask(__name__, static_folder='static')  # Specify the static folder
print("Flask app initialized...")

@app.route('/')
def home():
    print("Handling the home route...")
    return render_template('index.html')

if __name__ == '__main__':
    print("Running the app in debug mode...")
    app.run(debug=True)