from flask import Flask

# Create an instance of our app
app = Flask(__name__)

students = [
    {"id": 0, "title": "Mr.", "first_name": "Ben", "last_name": "Gilbert", "course": "DevOps"}
]


# decorator - to create our api/url for usr to access our data in the browser
@app.route("/")  # localhost:5000 is default port for Flask
def home():
    return "This is a dream team of DevOps consultants celebrating a WOW moment!!! "


# This function runs when the URL/API is accessed

if __name__ == "__main__":
    app.run(debug=True)
