'''
Topics-
- How to include Static Files on Website
- How to render HTML & CSS files
- 
'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

# All the images,static files, css files should be stored in the static folder.
# All the HTML files should be stored in the templates folder.