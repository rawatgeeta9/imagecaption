
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/about')
def about():
    aboutme={"name":"Geeta","Qualification":"MCA","Skillset":{"main":"Teaching","Secondary":"Cooking"}}
    return aboutme
@app.route('/login')
def login():
   return render_template('login/login.html')
@app.route('/usercheck',methods =[ "POST"])
def usercheck():
   if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
       last_name = request.form.get("lname") 
       return "Your name is "+first_name + last_name
   return render_template('login/login.html')
if __name__=="__main__":
    app.run(debug=True)