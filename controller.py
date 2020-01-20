import model
import view
import datetime 
import sqlite3
import datbas

class User():
	def __init__(self):
		self.username=None
		self.password=None
		self.userId=None
		self.access=None
		
	def Login(self):
		view.Statement("")
		self.username=input(view.QueryString('Username'))
		self.password=input(view.QueryString('Password'))
		status,self.userId=model.GetUserInfo(self.username,self.password)
		if status=='Fail':
			view.InvalidStatement('username and password','Main Menu')
			return MainMenu()
		return StudentMenu()
		

	def NewUser(self,access):
		self.username=input(view.QueryString('Username'))
		self.password=input(view.QueryString('Password'))
		self.access=access
		status,self.username=model.AddUserInfo(self.username,self.password,self.access)
		if status=='Fail':
			view.Statement(self.username+" already exist. Returning to Main Menu !")
			return MainMenu()
		else:
			view.Statement(self.username+" added")
			return MainMenu()

	def ForgotPassword(self):
		self.username=input(view.QueryString('Username'))
		status,self.password=model.GetUserPassword(self.username)
		if status=='Fail':
			return view.Statement('User not in database')
		else:
			return view.Statement("Your Password is :"+self.password) 

def MainMenu():
	choice=input(view.ShowMainMenu())
	if choice=='L' or choice=='l':
		tempUser.username=tempUser.Login()
		view.start()
		StudentMenu()
	elif choice=='N' or choice=='n':
		tempUser.NewUser('user')
		return MainMenu()
	elif choice=='E' or choice=='e':
		tempUser.ForgotPassword()
		return MainMenu()
	elif choice=='A' or choice=='a':
		LibraryMenu()
		view.lib()
	elif choice=='Q' or choice=='q':
		quit()
	else:
		view.InvalidStatement("Entry","Main Menu")	
		MainMenu()
   

def returnBook():
    model.ReturnBooks()
    print("The books have been returned succesfully, visit us again !")

def displayBook():
    model.bookStock()

def DeleteUser():
	model.DeleteUser(tempUser)

def addbooks():
	model.addbooks()

def StudentMenu():
		a=int(input(view.start()))

		if (a==1): 
			displayBook()
        
		elif (a==2) :
			borrowBook()
        
		elif (a==3):
			returnBook()
        
		elif (a==4):
			DeleteUser()                
        
		elif (a==5):
			print("Thank you for using library management system")
			quit()
        
		else:
			print("Please enter a valid choice from 1-4")
    

def LibraryMenu():
	b=input(view.lib())
	
	try:
		print()

		if (b==1):
			displayBook()
		
		elif (b==2) :
			DeleteUser()

		elif (b==3) :
			addbooks()

		elif (b==4) :
			model.finecheck()
		else:
			print("Please Enter a Valid Choice:") 
    
	except ValueError:
            print("Please input as suggested.")

def borrowBook():

	name=input("Enter the name of the librarian: ")
	con=sqlite3.connect('library.db')
	c=con.cursor()
	c.execute("SELECT Name FROM librarianDB WHERE [Name]=(:uname)",{'uname':name})
	list=c.fetchall()
	
	if list!=[] :
		 model.bookStock()
		 model.RentBooks(tempUser.username)
		 print('\n',"You have rented the book succesfully")
	
	else:
		print("The Librarian does not exist in the database TRY AGAIN !!")

	con.commit()
	con.close()		 


tempUser=User()

MainMenu()



            
    