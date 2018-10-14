from flask import Flask
from flask import render_template
from flask import url_for
app = Flask(__name__)

@app.route("/")
def abtme():
    abt = "About Me"
    git = """You can find more about me in the below Git hub link """
    phn = "9035320470"
    email = "jithin.abraham3@gmail.com"
    link = "https://github.com/jdeath777/python101"
    greeting = """ Hello people,
    This is Jithin here. A computer science engineer and a developer by 
    mistake.
    
    A hard core gamer by nature...... likes to read novels but not the typical 
    romantic once.
    Loves long bike rides
    Did my internship at Campus Management international for a Year.
    Now i work Full time for the same as an implementation engineer."""
    return render_template("abtme.html", greeting=greeting,abt=abt,git=git,phn=phn,
            email=email,link=link)

if __name__ == "__main__":
    app.run()
