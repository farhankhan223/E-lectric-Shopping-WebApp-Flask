from flask import Flask, render_template,request, redirect
import pymysql as p


def getconnect():
    return p.connect(host="localhost",user="root",password="",database="mkpbatchoct24")

    
def getdata():
    db = getconnect()
    cr = db.cursor()
    sql = "select name , password from user"
    cr.execute(sql)
    data = cr.fetchall()

    db.commit()
    db.close()
    return data

def insertdata(t):
    db = getconnect()
    cr = db.cursor()

    sql = "insert into user values(%s, %s, %s, %s, %s)"
    cr.execute(sql,t)
    db.commit()
    db.close()



def getalldata():
    db = getconnect()
    cr = db.cursor()

    sql = "select * from user"
    cr.execute(sql)
    data = cr.fetchall()

    db.commit()
    db.close()
    return data


def getadmindata():
    db=getconnect()
    cr=db.cursor()
    sql = "select name , password from admin"
    cr.execute(sql)
    data = cr.fetchall()
    db.commit()
    db.close()
    return data







########################### FLASK #########################
app = Flask(__name__)




@app.route("/")
def login():
    return render_template("page4.html")

@app.route("/login")
def logged():
    return render_template("page1.html")

@app.route("/registration")
def register():
    return render_template("page2.html")

@app.route("/validateuser", methods=["POST"])
def valid_user():
    usern = request.form["uname"]
    pasw = request.form["pin"]

    data = (usern,pasw)
    database = getdata()

    if(data in database):
        return render_template("page4.html")
    else:
        return render_template("page2.html")


@app.route("/insertrec", methods=["POST"])
def signup():
    ids = request.form["id"]
    uname = request.form["uname"]
    email = request.form["email"]
    add = request.form["address"]
    pasw = request.form["pin"]

    t = (ids,uname,email,add,pasw)
    insertdata(t)
    return redirect("registration")
    

@app.route("/user")
def users_list():
    userlist = getalldata()
    return render_template("user.html",ulist = userlist)


@app.route("/login2")
def lmn():
    return render_template("login2.html")

@app.route("/samsung")
def sl():
    return render_template("samsung.html")


@app.route("/iphone")
def i():
    return render_template("iphone.html")

@app.route("/xiaomi")
def x():
    return render_template("xiaomi.html")



@app.route("/asus")
def a():
    return render_template("asus.html")


@app.route("/hp")
def h():
    return render_template("hp.html")

@app.route("/dell")
def d():
    return render_template("dell.html")





@app.route("/usbcable")
def u():
    return render_template("usbcable.html")


@app.route("/laptopbags")
def l():
    return render_template("laptopbags.html")

@app.route("/charger")
def c():
    return render_template("charger.html")


@app.route("/validdd", methods=["POST"])
def validuser():
    usern = request.form["username"]
    pasw = request.form["password"]

    data = (usern,pasw)
    database = getadmindata()

    if(data in database):
        return render_template("user.html")
    else:
        return render_template("page2.html")





















if(__name__=="__main__"):
    app.run(debug=True)


