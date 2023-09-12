# import section
import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

# built-in variable first argument of Flask class,
# important for Flask to look fro templates and static files.
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

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
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")

@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

# One thing to take note. Never have debug=True in a production application or
# when to submit projects for assessment.
# Because it can allow arbitrary code to be run, this is a security flaw.
# Only have debug=True while testing the application in development mode.