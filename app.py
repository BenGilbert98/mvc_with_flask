from flask import Flask, jsonify, redirect, url_for, render_template

# Create an instance of our app
app = Flask(__name__)

students = [
    {"id": 0, "title": "Mr.", "first_name": "Ben", "last_name": "Gilbert", "course": "DevOps"}
]


# decorator - to create our api/url for usr to access our data in the browser
@app.route("/")  # localhost:5000 is default port for Flask
def home():
    return "<h1>This is a dream team of DevOps consultants celebrating a WOW moment!!!</h1> "


@app.route("/welcome/")  # http://127.0.0.1:5000/welcome/
def greet_user():
    return render_template("welcome.html")


# This function runs when the URL/API is accessed

# Creating our own API to display data on the specific route / URL / End point / API
@app.route("/api/v1/student/data/",
           methods=["GET"])  # This will add this API / URL to  http://127.0.0.1:5000/api/v1/student/data
def customised_api():
    return jsonify(students)  # transforms data into Json
    # Utilising Extract Transform Load


@app.route("/login/")
def login():
    return redirect(url_for("greet_user"))


@app.route("/<username>/")
def welcome_user(username):
    return f"<h1>Welcome to the dream team of DevOps {username}</h1>"


# @app.route("/redirect")
# def redirected():
#     return redirect("/welcome/")


# find out the module to redirect user back to specific page (welcome page)
# if page is not found (404) redirect user to welcome page


@app.route("/index/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

# create a base.html file in templates folder
# copy index.html to base.html
# google how to extend code from base.html to index.html
# Create text boxes for login form
