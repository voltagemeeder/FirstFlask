from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
    return 'Hello, World!'

@app.route('/bye')
def bye():
    # Retrieve username / passowrd from the request object.
    # Lookup user in database.
    # Return date of birth.
    return 'bye bye xxx'

app.run(debug=True)

# way to add things in a list
# way to display that list
# 