# import section
import os
from flask import Flask, render_template

# built-in variable first argument of Flask class,
# important for Flask to look fro templates and static files.
app = Flask(__name__)

# a route decorator binds by (wrapping functions) @ pie-notation symbol
#  the '/' returns from the top level of our domain, the template from our index function
@app.route("/")
def index():
    return render_template("index.html")


# the '/about' takes the template from our about.html file
# in order for the navigation link to work, 
# we need ninja templates method of url_for to call the appropriate functions.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/careers")
def careers():
    return render_template("careers.html")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

# One thing to take note. Never have debug=True in a production application or
# when to submit projects for assessment.
# Because it can allow arbitrary code to be run, this is a security flaw.
# Only have debug=True while testing the application in development mode.