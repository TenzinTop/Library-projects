import sqlite3
from datetime import datetime

con = sqlite3.connect('library.db')
c=con.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS userDB(
		[UserID] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
		[Username] VARCHAR NOT NULL, 
		[Password] VARCHAR NOT NULL,
		[Access] INTEGER NOT NULL,
		[LogInTime] REAL);""")

c.execute("""CREATE TABLE IF NOT EXISTS librarianDB(
	    [Librarian_Counter]INTEGER PRIMARY KEY NOT NULL,
		[Name] VARCHAR NOT NULL,
        [Contact] INT NOT NULL);""")

c.execute("""CREATE TABLE IF NOT EXISTS booksDB(
                [Author_Name] VARCHAR NOT NULL,
                [Book_name] VARCHAR NOT NULL,
                [Rented_to] VARCHAR,
				[Rented_Date] REAL
				 );""")


con.commit()
con.close()      
