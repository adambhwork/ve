from flask import Flask, render_template
import mysql.connector
from flask_bootstrap import Bootstrap
import json
import requests


app = Flask(__name__)
bootstrap=Bootstrap(app)

#mydb = mysql.connector.connect(host='35.242.137.212', user="root", password="",database="VE")#GoogleCloud#
mydb = mysql.connector.connect(host='Adambh.mysql.pythonanywhere-services.com', port=3306,  user="Adambh", password="London100",database="Adambh$VE")


if mydb:
    print ("Connected Successfully")
else:
    print ("Connection Not Established")
mycursor = mydb.cursor()


comments=[]

@app.route('/')
def index():
   return render_template('html_test.html')

@app.route('/home', methods=['GET','POST'])
def home():
   return render_template('html_test.html')

@app.route('/destinations', methods=['GET','POST'])
def bookacoach():
    return render_template('destinations.html')

@app.route('/contactus')
def contactus():
   return render_template('contactus.html')

@app.route('/oxford')
def oxford():
   return render_template('oxford.html')

@app.route('/cambridge')
def cambridge():
   return render_template('cambridge.html')

@app.route('/exeter')
def exeter():
   return render_template('exeter.html')

@app.route('/stives')
def stives():
   return render_template('stives.html')

@app.route('/windsor')
def windsor():
   return render_template('windsor.html')

@app.route('/windsoreat')
def windsoreat():
    select_restaurants = """SELECT name,style, address, contact FROM restaurants where place=5"""
    mycursor.execute(select_restaurants)
    data = mycursor.fetchall()
    return render_template("example.html", value=data)

@app.route('/oxfordeat')
def oxfordeat():
    select_restaurants = """SELECT name,style, address, contact FROM restaurants where place=2"""
    mycursor.execute(select_restaurants)
    data = mycursor.fetchall()
    return render_template('oxfordeat.html', value=data)

@app.route('/cambridgeeat')
def cambridgeeat():
    select_restaurants = """SELECT name,style, address, contact FROM restaurants where place=3"""
    mycursor.execute(select_restaurants)
    data = mycursor.fetchall()
    return render_template('cambridgeeat.html', value=data)

@app.route('/exetereat')
def exetereat():
   select_restaurants = """SELECT name,style, address, contact FROM restaurants where place=6"""
   mycursor.execute(select_restaurants)
   data = mycursor.fetchall()
   return render_template('exetereat.html', value=data)

@app.route('/stiveseat')
def stiveseat():
    select_restaurants = """SELECT name,style, address, contact FROM restaurants where place=4"""
    mycursor.execute(select_restaurants)
    data = mycursor.fetchall()
    return render_template('stiveseat.html', value=data)

@app.route('/windsortodo')
def windsortodo():
    select_todo = """SELECT name,address, contact FROM todo where place=5"""
    mycursor.execute(select_todo)
    data = mycursor.fetchall()
    return render_template('windsortodo.html', value=data)

@app.route('/oxfordtodo')
def oxfordtodo():
    select_todo = """SELECT name,address, contact FROM todo where place=2"""
    mycursor.execute(select_todo)
    data = mycursor.fetchall()
    return render_template('oxfordtodo.html', value=data)

@app.route('/cambridgetodo')
def cambridgetodo():
    select_todo = """SELECT name,address, contact FROM todo where place=3"""
    mycursor.execute(select_todo)
    data = mycursor.fetchall()
    return render_template('cambridgetodo.html', value=data)

@app.route('/exetertodo')
def exetertodo():
    select_todo = """SELECT name,address, contact FROM todo where place=6"""
    mycursor.execute(select_todo)
    data = mycursor.fetchall()
    return render_template('exetertodo.html', value=data)

@app.route('/stivestodo')
def stivesodo():
    select_todo = """SELECT name,address, contact FROM todo where place=4"""
    mycursor.execute(select_todo)
    data = mycursor.fetchall()
    return render_template('stivestodo.html', value=data)

@app.route('/windsortravel')
def windsortravel():
    req=requests.get("https://storage.googleapis.com/damdata/VEngland2/destinationsinfo/windsor.json")
    #data=json.loads(req.content)
    data = json.loads(req.content.decode('utf-8'))
    x=data.items()
    return render_template ('windsortravel.html', x=x)

@app.route('/stivestravel')
def stivestravel():
    req=requests.get("https://storage.googleapis.com/damdata/VEngland2/destinationsinfo/stives.json")
    #data=json.loads(req.content)
    data = json.loads(req.content.decode('utf-8'))
    x=data.items()
    return render_template ('stivestravel.html', x=x)

@app.route('/oxfordtravel')
def oxfordtravel():
    req=requests.get("https://storage.googleapis.com/damdata/VEngland2/destinationsinfo/oxford.json")
    #data=json.loads(req.content)
    data = json.loads(req.content.decode('utf-8'))
    x=data.items()
    return render_template ('oxfordtravel.html', x=x)

@app.route('/exetertravel')
def exetertravel():
    req=requests.get("https://storage.googleapis.com/damdata/VEngland2/destinationsinfo/exeter.json")
    #data=json.loads(req.content)
    data = json.loads(req.content.decode('utf-8'))
    x=data.items()
    return render_template ('exetertravel.html', x=x)

@app.route('/cambridgetravel')
def cambridgetravel():
    req=requests.get("https://storage.googleapis.com/damdata/VEngland2/destinationsinfo/cambridge.json")
    #data=json.loads(req.content)
    data = json.loads(req.content.decode('utf-8'))
    x=data.items()
    return render_template ('cambridgetravel.html', x=x)


if __name__ == "__main__":
   app.run(debug=False)
