import sqlite3
con=sqlite3.connect('library.db')
c=con.cursor()

c.execute("INSERT INTO  librarianDB (Librarian_Counter,Name,Contact)\
        VALUES(1,'Vivek',90008000)")   
c.execute("INSERT INTO librarianDB (Librarian_Counter,Name,Contact)\
        VALUES(2,'Ash',90111000)")   
c.execute("INSERT INTO librarianDB (Librarian_Counter,Name,Contact)\
       VALUES(3,'Tenzin',123456789)") 

c.execute("INSERT INTO booksDB (Author_name,Book_name,Rented_Date)\
			VALUES('PAULO COELHO','THE ALCHEMIST','05/01/2020')")
c.execute("INSERT INTO booksDB (Author_name,Book_name,Rented_Date)\
			VALUES('SIDNEY SHELDON','STARS','NULL')")
c.execute("INSERT INTO booksDB (Author_name,Book_name,Rented_Date)\
			VALUES('GREEN','FAULT IN OUR STARS','07/01/2020')")

con.commit()
con.close()