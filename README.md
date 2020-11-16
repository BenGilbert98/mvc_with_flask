# MVC with Flask in Python

# MVC (Model View Controller)
Display data on the browser using HTML, CSS, JS and BOOTSTRAP.

- HTML - Hyper Text markup language
- CSS - Cascading Style Sheet
- JS - Javascript
- BOOTSTRAP

**Building our API**
- display data from python flask to specific API call / URL / end point /

**Why Flask and Use Cases**
- Flask is a web app frame work
- Very powerful to interact with DB and user interface / browsers etc
- Flask can be used to create an API 
- It allows us to integrate with HTML, CSS, JS etc
- It allows us to map HTTP requests to Python functions -URL -HTTP  GET
- Allows us to set API path as a URL to view in the browser
- Flask looks for lower case app file name

### Installing flask 
``` python
pip install flask
```
### Run the flask app - command
```
flask run
```
### Creating Instance of App
- instance of app is created using ```app = Flask(__name__)```
- students data is then defined
```python
app = Flask(__name__)

students = [
    {"id": 0, "title": "Mr.", "first_name": "Ben", "last_name": "Gilbert", "course": "DevOps"}
]
```
### Setting up a home page
- @app.route is used to specify the url for the page
- def home() is a function that prints ```This is a dream team of DevOps consultants celebrating a WOW moment!!!```
- ```<h1> </h1>``` is used to display the string as a title.
```python
@app.route("/")  # localhost:5000 is default port for Flask
def home():
    return "<h1>This is a dream team of DevOps consultants celebrating a WOW moment!!!</h1> "
```

### Welcome page
- the decorator @app.route("/welcome/") is used to create a welcome page
- the function greet_user(): is used to return a message of "Welcome to DevOps team" (displayed on the page)
``` python
@app.route("/welcome/")
def greet_user():
    return "Welcome to DevOps team"
```

### Data page
- Creating our own API to display data on the specific route / URL / End point / API
- customised_api() is used to return a json version of the students
```python
@app.route("/api/v1/student/data/",
           methods=["GET"])  # This will add this API / URL to  http://127.0.0.1:5000/api/v1/student/data
def customised_api():
    return jsonify(students)  # transforms data into Json
```

### Redirect
- API is defined which will redirect the user to the welcome api from "/login/"
```python
@app.route("/login/")
def login():
    return redirect(url_for("greet_user"))
```

### Username
- API which will welcome the user
- "/<username>/" is used as a replacement for the user input
``` python
@app.route("/<username>/")
def welcome_user(username):
    return f"<h1>Welcome to the dream team of DevOps {username}</h1>"
```