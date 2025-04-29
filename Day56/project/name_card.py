'''Name Card Project'''

# Download Template
# Unzip file and get access to all files inside.
# Set up flask server
# Create a folder named static and templates in the same directory as your main.py file.
# Move the index.html file to the templates folder and all the images, css files to the static folder.
# Change path if needed
# Run the server and check if everything is working fine.
# Make the necessary changes like name, images etc.
# Add background images also, if needed.
# Link is - https://html5up.net/editorial


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)