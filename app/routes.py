from flask import Flask  # from the flask module import the Flask class.

app = Flask(__name__) #instantiate the Flask class into the app variable.
                      #Variables that contain class instances are called "objects".

@app.route("/")                     #This is a decorator
def index():                        #this is a function; flask calls it a "View function"
    return"<h1>hello, world!<h1>"   #just a return statement; returning a string



@app.get("/home")
def home():
    return "welcome Home!"


@app.route ("/about", methods = ["GET"])
def about():
    return "Hi my name is Eric."