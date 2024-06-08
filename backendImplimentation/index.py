from flask import Flask
from flask import Flask,render_template
app = Flask(__name__)
@app.route("/login")
def test_case():
      return render_template("login.html")

@app.route("/register")
def test_case1():
      return render_template("register.html")

if(__name__=="__main__"):
      app.run(debug=True)
   