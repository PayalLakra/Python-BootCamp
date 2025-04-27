'''Topics to be Covered:
- How to render HTML on your website
- How to hold of and pass the URL.
- Advanced Decorators
- Flask Debugging
'''

# Python Decorators
from functools import wraps
from flask import Flask

app = Flask(__name__)

def make_bold(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return f"<b>{f(*args, **kwargs)}</b>"
    return decorated_function

def make_emphasis(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return f"<em>{f(*args, **kwargs)}</em>"
    return decorated_function

def make_underlined(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return f"<u>{f(*args, **kwargs)}</u>"
    return decorated_function

# Example usage
@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)