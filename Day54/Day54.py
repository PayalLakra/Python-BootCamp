# Flask- One of the most popular web frameworks for Python
# Python Decorators - A way to modify the behavior of a function or class method
# Functions are first-class objects in Python, meaning they can be passed around as arguments, returned from other functions, and assigned to variables.
# Functions can also be nested, meaning you can define a function inside another function.
# Functions can be returned as the output from another function without needing to trigger it.

# Basic Flask App
from flask import Flask
app = Flask(__name__)

@app.route('/')     # This decorator creates a route for the root URL
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == '__main__':
    app.run()  # Run the app for development

# A Decorator function is simply a function which wraps another function, modifying its behavior.