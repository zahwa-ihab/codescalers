from flask import Flask, render_template , url_for, redirect
from ast import arg
from flask_mysqldb import MySQL

import backend.userinfo as userinfo
# import MySQLdb 
import mysql.connector

class userinfo:
  def __init__(self):
    self.db=mysql.connector.connect(host="localhost",user="root",password="",database="codescalers")
  def  getdetails(self):
    #   excute=self.db.cursor()
    #   excute.callproc('userdetails')
    #   result=excute.fetchall()
    mycursor=self.db.cursor()

    mycursor.execute("SELECT *  From usersinfo ")
    myresult = mycursor.fetchall()

    return myresult
      
  def deleteEntry(self,id):
    mycursor=self.db.cursor()

    mycursor.execute("DELETE from usersinfo WHERE id=1")
    print("done deleting")

    #excute=self.db.cursor()
    #excute.callproc('deletentry', args=(id))


app = Flask(__name__)
user1 = userinfo()


@app.route('/')
def homepage():
    fetchedresults=user1.getdetails()
    print("hhhhhh")
    for x in fetchedresults:
         print(x)
    return render_template('index.html',data=fetchedresults)


@app.route('/delete/<int:data>', methods=['POST','GET'])
def delete(data):
     print("deleteees")
     user1.deleteEntry(data)
     return homepage()




# main driver function
if __name__ == '__main__':
  
    app.run()