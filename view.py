
def ShowMainMenu():
	print("\n---Welcome to Byte Library---")
	print("[L] : Login")
	print("[E] : Forgot Password")
	print("[N] : Create New Student user")
	print("[A] : Login as Librarian")
	print("[Q] : Quit Program")
	return "-->Enter Your Choice : "

def InvalidStatement(string,menu):
	print("\nInvalid "+string+".Returning to "+menu+" !")

def QueryString(string):
	return "Enter "+string+": "

def Statement(statement):
	print(statement)
	return

def start():
        print("        Welcome to the byte Library     ")
        print("1:. To Display")
        print("2:. To Borrow a book")
        print("3:. To return a book")
        print("4:  Delete user")
        print("5:. To exit")
        return"----Enter Your choice:"

def ShowAllUsers(userList):
	for item in userList:
		print(item)
	print("Returning to  Menu")
	return

def lib():
        print("        Welcome  Librarian")
        print("1:. To Display")
        print("2:. To delete user")
        print("3:. add new books")
        print("4:  fine check")
        return "----Enter your choice:"
    