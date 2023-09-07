# import section
import os
from flask import Flask

# built-in variable first argument of Flask class, important for Flask to look fro templates and static files.
app = Flask(__name__)

# a route decorator(wrapping functions) @ pie-notation symbol
@app.route("/")
def index():
    return "Hello World"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5500")),
        debug=True)
    
# One thing to take note. Never have debug=True in a production application or
# when to submit projects for assessment.
# Because it can allow arbitrary code to be run, this is a security flaw.
# Only have debug=True while testing the application in development mode.