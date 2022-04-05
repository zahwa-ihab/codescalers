from ast import arg
import MySQLdb 

class userinfo:
  def __init__(self):
    self.db=MySQLdb.connect("localhost","root","","codescalers")

  def  getdetails(self):
      excute=self.db.cursor()
      excute.callproc('userdetails')
      result=excute.fetchall()

      return result
      
  def deleteEntry(id):
    excute=self.db.cursor()
    excute.callproc('deletentry', args=(id))
    print( excute.callproc('deletentry', args=(id)))
    return "deleted"






