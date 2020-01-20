import sqlite3
import datbas
import view
from datetime import datetime 
from datetime import date

def GetUserInfo(username,password):
	conn=sqlite3.connect('library.db')
	c=conn.cursor()
	c.execute("SELECT [UserId],[Username],[Password] FROM userDB WHERE [Username]=(:uname) AND [Password]=(:pass)",{'uname':username,'pass':password})
	myList=c.fetchall()
	conn.close()
	if myList==[]:
		return 'Fail',None
	else:
		return 'Success',myList[0][0]

def AddUserInfo(username,password,access):
	conn=sqlite3.connect('library.db')
	c=conn.cursor()
	c.execute("SELECT [UserId],[Username],[Password] FROM userDB WHERE [Username]=(:uname)",{'uname':username})
	myList=c.fetchall()
	login=datetime.now()
	if myList==[]:
		c.execute("INSERT INTO userDB([Username],[Password],[Access],[LogInTime]) VALUES(:uname,:pass,:access,:login)",{'uname':username,'pass':password,'access':access,'login':login})
		conn.commit()
		conn.close()
		return 'Success',username
	else:
		return 'Fail',username

def GetUserPassword(username):
	conn=sqlite3.connect('library.db')
	c=conn.cursor()
	c.execute("SELECT [Username],[Password] FROM userDB WHERE [Username]=(:uname)",{'uname':username})
	myList=c.fetchall()
	conn.close()
	if myList==[]:
		return 'Fail',None
	else:
		return 'Success',myList[0][1]

def GetUserAccess(username):
	conn=sqlite3.connect('library.db')
	c=conn.cursor()
	c.execute("SELECT [Username],[Password],[Access] FROM userDB WHERE [Username]=(:uname)",{'uname':username})
	myList=c.fetchall()
	conn.close()
	if myList==[]:
		return 'Fail',None
	else:
		return 'Success',myList[0][2]


def bookStock():
	conn= sqlite3.connect("library.db")
	c=conn.execute("SELECT Book_name,Rented_Date FROM booksDB ")
	for column in c:
		for i in column:
			i=0
			print("Books in this library are" ,column[i])
	conn.commit()
	conn.close()

def RentedBooks():
	con1= sqlite3.connect("library.db")
	cursor= con1.execute("SELECT Book_name,Rented_Date,Rented_to FROM booksDB WHERE Rented_Date=REAL")
	for column in cursor:
		for i in column:
			i=0
			print("Books as of now you can borrow are :",column[i])
	con1.commit()
	con1.close()

def RentBooks(username):
	con2= sqlite3.connect('library.db')
	c=con2.cursor()
	c.execute("SELECT Book_name,Rented_Date FROM booksDB WHERE Rented_Date='NULL'")
	c.execute("UPDATE booksDB set [Rented_Date]= (:date1), [Rented_to]=(:uname)",{'date1':date.now(),'uname':username})
	print("You have rented the book succesfully")
	con2.commit()
	con2.close()

def ReturnBooks():
	con3= sqlite3.connect('library.db')
	cursor= con3.execute("SELECT Book_name,Rented_Date FROM booksDB WHERE Rented_Date='REAL'")
	cursor.execute("UPDATE booksDB set Rented_Date= null ,Rented_to=''")
	con3.commit()
	con3.close()

def DeleteUserRow(username):
	conn=sqlite3.connect('library.db')
	c=conn.cursor()
	c.execute("DELETE FROM tradeDB WHERE [Username]=(:username)",{'username':username})
	c.execute("DELETE FROM userDB WHERE [Username]=(:username)",{'username':username})
	conn.commit()
	conn.close()

def DeleteUser(username):
	status,access=GetUserAccess(username)
	if access=='librarian':
		deletename=input(view.QueryString('Username to be deleted'))
		status,password=GetUserPassword(deletename)
		if status=='Success':
			view.Statement(deletename+" with password '"+password+"'' will be deleted")
			check=input(view.QueryString('Press Y to delete User'))
			if check=='Y' or check=='y':
				DeleteUserRow(deletename)
				view.Statement(deletename+" with password '"+password+"'' is now deleted !")
				return
		else:
			return view.Statement('User not in database')
	else:
		view.Statement("\nYou are not authorised to delete a user. Please contact Librarian.!")

def addbooks():
	authorname=print(input(str("Please enter the author name: ")))
	namebooks1=print(str(input("Please enter the book name:")))
	conn=sqlite3.connect('library.db')
	c=conn.cursor()
	c.execute("INSERT INTO booksDB([Author_name],[Book_name]) VALUES(:author,:book)",{'author':authorname,'book':namebooks1})
	print("Added books succesfully")
	conn.commit()
	conn.close()			

Fined=[]
def finecheck(username):
	
	today=date.today()
	con= sqlite3.connect('library.db')
	c1=con.cursor()
	rentdate=c1.execute("SELECT Rented_Date FROM booksDB ")	
	total=today-rentdate

	if (total>=30):
		print(username,"have past the 30 days mark and is",total,"total days Late")
		Fined='30'
		print(Fined)
	else:
		print("No fines as of now")	
