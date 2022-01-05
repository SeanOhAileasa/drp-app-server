user="__you_user___" # defaults to "root"
password="___your_password___" # default to ""
database="mysql" # default can leave

# from sys import path; path.insert(1,"./rc/server/") # location of dbconfig.py
# from dbconfig import nMySQL as cfg # using dbconfig.py parameters

try:
	from mysql.connector import connect # third-party library import
	
	#nObjMySQLConnection=connect(host=cfg["host"],
	#	user=cfg["username"],
	#	password=cfg["password"],
	#	database="mysql") # input dbconfig.py parameters

	nObjMySQLConnection=connect(host="localhost",
		user=user,
		password=password,
		database=database) # input your parameters

	nInsObjCursor=nObjMySQLConnection.cursor() # traveral over records
	nInsObjCursor.execute("show tables") # abstracts away access
	for nEachTable in nInsObjCursor:
	    print(nEachTable)
	nInsObjCursor.execute("drop database data_representation") # create table book	    
	nInsObjCursor.execute("CREATE DATABASE data_representation") # create table book
	nInsObjCursor.execute("use data_representation") # create table book
	nInsObjCursor.execute("CREATE TABLE book(id INT NOT NULL AUTO_INCREMENT,title VARCHAR(250),author VARCHAR(250),price INT,PRIMARY KEY(id))") # create table book
	nInsObjCursor.execute("INSERT INTO book (title,author,price) VALUES (\"THE JUDGE'S LIST\",\"John Grisham\",29)") # insert into table
	nInsObjCursor.execute("INSERT INTO book (title,author,price) VALUES (\"THE STRANGER IN THE LIFEBOAT\",\"Mitch Albom\",25)") # insert into table
	nInsObjCursor.execute("INSERT INTO book (title,author,price) VALUES (\"IT ENDS WITH US\",\"Colleen Hoover\",30)") # insert into table
	nInsObjCursor.execute("INSERT INTO book (title,author,price) VALUES (\"THE LINCOLN HIGHWAY\",\"Amor Towles\",50)") # insert into table
	nInsObjCursor.execute("INSERT INTO book (title,author,price) VALUES (\"CALL US WHAT WE CARRY\",\"Amanda Gorman\",15)") # insert into table
except ImportError:
	print("You Are Missing a Package (mysql-connector-python)")
	print("Please Install - Restart Application")
	print("$ pip install mysql-connector-python ")