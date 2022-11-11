from flask import Flask, render_template, redirect, url_for, request, flash, g, session
#from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from datetime import datetime
import sqlite3

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

""" # Required
app.config["MYSQL_USER"] = "user"
app.config["MYSQL_PASSWORD"] = "BubbyIsGooder1"
app.config["MYSQL_DB"] = "finance.db"
# Extra configs, optional:
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
app.config["MYSQL_CUSTOM_OPTIONS"] = {"ssl": {"ca": "/path/to/ca-file"}}  # https://mysqlclient.readthedocs.io/user_guide.html#functions-and-attributes

mysql = MySQL(app) """



currentMonth = datetime.now().month


db = sqlite3.connect("finance5.db", check_same_thread=False)
with db:
    cur = db.cursor()


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/loggedIndex", methods=["GET", "POST"])
def index2():
    #return str(session["id"])
    return render_template("loggedIndex.html")


@app.route("/data", methods=["GET", "POST"])
def data():

    if request.method == "POST":
        with db:
            db.execute("INSERT INTO cash (id, cash) VALUES (?,?)", [session["id"], request.form.get("cash")])
            db.commit()

            cur.execute("SELECT SUM(cash) FROM cash WHERE id = ?", [session["id"]])
            cash = cur.fetchall()
    


        render_template("data.html", cash=usd((cash[0][0])), month=currentMonth)

    with db:
        cur.execute("SELECT SUM(cash) FROM cash WHERE id = ?", [session["id"]])
        cash = cur.fetchall()

    if (cash[0][0]==None):
        return render_template("data.html", cash=usd(0))
    else:
        return render_template("data.html", cash = usd(cash[0][0]), month=currentMonth)


    

@app.route("/journal", methods=["GET", "POST"])
def journal():

    if request.method == "POST":

        if not (request.form.get("month")).isdigit():
            return apology("Need a month number", 400)
        
        if (int(request.form.get("month")) < 1) | (int(request.form.get("month")) > 12):
            return apology("Number must be between 1 and 12", 400)

        #return usd(float(request.form.get("price")))

        db.execute("INSERT INTO transactions (id, month ,type, name, price) VALUES (?,?,?,?,?)", [session["id"], request.form.get("month"), request.form.get("transactionType"), request.form.get("transactionName"), (usd(float(request.form.get("price"))))])
        db.commit()

        #cur.execute("SELECT SUM(cash) FROM cash WHERE id = ?", [session["id"]])
        #cash = cur.fetchall()

        db.execute("INSERT INTO cash (id, cash) VALUES (?,?)", [session["id"],-float(request.form.get("price"))]) 
        db.commit()
        
        cur.execute("SELECT month ,type, name, price FROM transactions WHERE id = ? ORDER BY purchaseNum DESC", [session["id"]])
        transactionHistories = cur.fetchall()
  
        

        cur.execute("SELECT SUM(price) FROM transactions WHERE type = ? AND id = ? AND month = ?", ["Savings", session["id"], currentMonth])
        savingsCost = cur.fetchall()

        cur.execute("SELECT SUM(price) FROM transactions WHERE type = ? AND id = ? AND month = ?", ["Wants", session["id"], currentMonth])
        wantsCost = cur.fetchall()

        cur.execute("SELECT SUM(price) FROM transactions WHERE type = ? AND id = ? AND month = ?", ["Needs", session["id"], currentMonth])
        needsCost = cur.fetchall()


        #cost = savingsCost + wantsCost + needsCost
        if (savingsCost[0][0] != None):
            savingsCost = usd(savingsCost[0][0])
        else:
            savingsCost = usd(0)
    
        if (wantsCost[0][0] != None): 
            wantsCost = usd(wantsCost[0][0])
        else:
            wantsCost = usd(0)
        
        if (needsCost[0][0] != None):
            needsCost = usd(needsCost[0][0])
        else:
            needsCost = usd(0)

        return render_template("journal.html", transactionHistories = transactionHistories, savingsCost = savingsCost, wantsCost=wantsCost, needsCost=needsCost)

    #today = date.today()
    #print("today's date:", today)

    cur.execute("SELECT month,type, name, price FROM transactions WHERE id = ? ORDER BY purchaseNum DESC", [session["id"]])
    transactionHistories = cur.fetchall()

    cur.execute("SELECT SUM(price) FROM transactions WHERE type = ? AND id = ? AND month = ?", ["Savings", session["id"], currentMonth])
    savingsCost = cur.fetchall()

    cur.execute("SELECT SUM(price) FROM transactions WHERE type = ? AND id = ? AND month = ?", ["Wants", session["id"], currentMonth])
    wantsCost = cur.fetchall()

    cur.execute("SELECT SUM(price) FROM transactions WHERE type = ? AND id = ? AND month = ?", ["Needs", session["id"], currentMonth])
    needsCost = cur.fetchall()
   

    #return str(usd(savingsCost[0][0]) + usd(wantsCost[0][0]) + usd(needsCost[0][0]))

    if (savingsCost[0][0] != None):
        savingsCost = usd(savingsCost[0][0])
    else:
        savingsCost = usd(0)
    
    if (wantsCost[0][0] != None): 
        wantsCost = usd(wantsCost[0][0])
    else:
        wantsCost = usd(0)
        
    if (needsCost[0][0] != None):
        needsCost = usd(needsCost[0][0])
    else:
        needsCost = usd(0)

    #cost = savingsCost[0][0] + wantsCost[0][0] + needsCost[0][0]
 
    return render_template("journal.html", transactionHistories = transactionHistories, savingsCost = savingsCost, wantsCost = wantsCost, needsCost = needsCost)

@app.route("/quick_add", methods=["GET", "POST"])
def quick_add():
    if request.method == "POST":
        #request.form.get("transactionType")
        #request.form.get("transactionName")
        #request.form.get("price")

        db.execute("INSERT INTO transactions (id, month ,type, name, price) VALUES (?,?,?,?,?)", [session["id"], currentMonth, request.form.get("transactionType"), request.form.get("transactionName"), (usd(float(request.form.get("price"))))])
        db.commit()

        cur.execute("SELECT month,type, name, price FROM transactions WHERE id = ? ORDER BY purchaseNum DESC", [session["id"]])
        transactionHistories = cur.fetchall()

        cur.execute("SELECT SUM(price) FROM transactions WHERE type = ? AND id = ? AND month = ?", ["Savings", session["id"], currentMonth])
        savingsCost = cur.fetchall()

        cur.execute("SELECT SUM(price) FROM transactions WHERE type = ? AND id = ? AND month = ?", ["Wants", session["id"], currentMonth])
        wantsCost = cur.fetchall()

        cur.execute("SELECT SUM(price) FROM transactions WHERE type = ? AND id = ? AND month = ?", ["Needs", session["id"], currentMonth])
        needsCost = cur.fetchall()

        if (savingsCost[0][0] != None):
            savingsCost = usd(savingsCost[0][0])
        else:
            savingsCost = usd(0)
    
        if (wantsCost[0][0] != None): 
            wantsCost = usd(wantsCost[0][0])
        else:
            wantsCost = usd(0)
        
        if (needsCost[0][0] != None):
            needsCost = usd(needsCost[0][0])
        else:
            needsCost = usd(0)

        return render_template("journal.html", transactionHistories = transactionHistories, savingsCost = savingsCost, wantsCost = wantsCost, needsCost = needsCost)

    cur.execute("SELECT month, type, name, price FROM transactions WHERE id = ? GROUP BY name HAVING COUNT(name) > 2", [session["id"]])
    transactionsAboveFive = cur.fetchall()


    return render_template("quick_add.html", transactionsAboveFive = transactionsAboveFive)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        #All input fields must be present
        if (len(request.form.get("name")) == 0) | (len(request.form.get("username")) == 0) | (len(request.form.get("password"))==0):
            return apology("One of the input fields was left blank!", 400)

        #Password and password confirmation must match        
        if ((request.form.get("password")) != (request.form.get("confirmation"))):
            return apology("Passwords do not match", 400)

        with db:
            cur.execute("SELECT * FROM users WHERE username = ?", [request.form.get("username")])
            rows = cur.fetchall()

        #if username matches another username
        if len(rows) >= 1:
            return apology("Username is already taken", 400)

        #if there are no errors, then the username and password will be registered

        with db:
            db.execute("INSERT INTO users (name, username, password) VALUES (?,?,?)", (request.form.get("name"), request.form.get("username"), request.form.get("password")))
            db.commit()
        

        #return to the login screen 
        
        return render_template("login.html")
    

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #request.form.get("username")
        #request.form.get("password")


        cur.execute("SELECT username, password FROM users WHERE username = ? AND password = ?", [request.form.get("username"), request.form.get("password")])
        rows = cur.fetchall()
    

        cur.execute("SELECT id FROM users WHERE username = ?", [request.form.get("username")])
        id = cur.fetchall()

        if len(rows) >= 1:
            session["id"] = id[0][0]
            return render_template("loggedIndex.html")
        else:
            return apology("Incorrect Username and/or Password")
    
    return render_template("login.html")

@app.route("/logout", methods=["GET","POST"])
def logout():
    flash("You have been logged out", 'danger')
    return render_template("index.html")

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=message)

def usd(amt):
    return "{:.2f}".format(amt)

