from mysql.connector import connect
from dbconfig import nMySQL as cfg
# define class - CBookDAO
class CBookDAO: # blueprint state functionality
	nClsAttDB="" # for all instances
	def __init__(self): # initialise object state
		""" Using class attribute to create default value (state).
	Input: object itself (self)
	Process: nClsAttDB
	Output: called automatically when creating a new instance of CBookDAO
	"""
		self.nClsAttDB=connect(host=cfg["host"],user=cfg["username"],password=cfg["password"],database=cfg["database"]) # establish a connection		
		print("<Connection Successful>")
	def fInsMetCreate(self,nInsAttJSON):
		""" Create record from JSON object passed (and extract).
	Input: object itself (self); nInsAttJSON
	Process: nClsAttDBC
	Output: record created and return id
	"""		
		nInsObjCursor=self.nClsAttDB.cursor() # traveral over records
		sqlQuery="INSERT INTO book (title,author,price) VALUES (%s,%s,%s)"
		nValues=[nInsAttJSON["title"],nInsAttJSON["author"],nInsAttJSON["price"]]
		nInsObjCursor.execute(sqlQuery,nValues) # abstracts away access
		self.nClsAttDB.commit() # commit current transaction
		return nInsObjCursor.lastrowid
	def fInsMetGetAllTuple(self):
		""" Return all records (as tuples).
		Requires converting the tuples manually into a collection of dict objects (later converting to JSON).
	Input: object itself (self)
	Process: nClsAttDB
	Output: show all records as a collection of tuples
	"""			
		nInsObjCursor=self.nClsAttDB.cursor()
		nInsObjCursor.execute("SELECT * FROM book")
		return nInsObjCursor.fetchall()
	def fInsMetConvert2Dict(self,nInsAttResult):
		""" Iterate and extract from table book its column names to make a dict object.
		Can send the dict object to HTML later.
	Input: object itself (self); nInsAttResult
	Process: nClsAttDB; 
		a. create list of column names;
		b. create dict object;
		c. test NULL not passed (check nInsAttResult exists);
		d. iterate column names one at a time using a.) number and b.) names;
		e. enumerate through the columns names and;
		f. extract value from nInsAttResult and assign item that matches it 
	Output: show all records as a collection of dicts
	"""	
		nColumnNames=["id","title","author","price"]
		nBookDict={}
		if nInsAttResult:
			for i,nEachName in enumerate(nColumnNames):
				nValues=nInsAttResult[i]
				nBookDict[nEachName]=nValues
		return nBookDict
	def fInsMetGetAllDict(self):
		""" Replace fInsMetGetAllTuple to return all records (as dict).
	Input: object itself (self)
	Process: nClsAttDB; fInsMetConvert2Dict
	Output: show all records as a collection of dict objects
	"""			
		nInsObjCursor=self.nClsAttDB.cursor()
		nInsObjCursor.execute("SELECT * FROM book")
		nResult=nInsObjCursor.fetchall() # return a tuple
		nCollectionDict=[]
		for nEachResult in nResult:
			nCollectionDict.append(self.fInsMetConvert2Dict(nEachResult)) # convert dict object
		return nCollectionDict
	def fInsMetGetByID(self,nInsAttID):
		""" Find record by ID via tuple (converting to dict).
	Input: object itself (self); nInsAttID
	Process: nClsAttDB; fInsMetConvert2Dict
	Output: show record by ID
	"""			
		nInsObjCursor=self.nClsAttDB.cursor()
		nInsObjCursor.execute("SELECT * FROM book WHERE id=%s",(nInsAttID,))
		return self.fInsMetConvert2Dict(nInsObjCursor.fetchone())
	def fInsMetUpdate(self,nInsAttDict):
		""" Passing dict object update record.
	Input: object itself (self); nInsAttDict
	Process: nClsAttDB
	Output: update record by dict object
	"""			
		nInsObjCursor=self.nClsAttDB.cursor()
		nNameValue=[nInsAttDict["title"],nInsAttDict["author"],nInsAttDict["price"],nInsAttDict["id"]] # match query order
		nInsObjCursor.execute("UPDATE book SET title=%s,author=%s,price=%s WHERE id=%s",nNameValue)
		self.nClsAttDB.commit()
		return nInsAttDict
	def fInsMetDeleteTuple(self,nInsAttID):
		""" Using the values (%s) from somewhere passed in as a tuple executing as a variable delete record.
	Input: object itself (self); nInsAttID
	Process: nClsAttDB
	Output: record deleted
	"""
		nInsObjCursor=self.nClsAttDB.cursor()
		nInsObjCursor.execute("DELETE FROM book where id=%s",(nInsAttID,))
		self.nClsAttDB.commit()
		return {}
	def fInsMetDeleteJSON(self,nInsAttJSON):
		""" Passing dict index id object to delete record.
	Input: object itself (self); nInsAttJSON
	Process: nClsAttDB
	Output: record deleted
	"""
		nInsObjCursor=self.nClsAttDB.cursor()
		n=[nInsAttJSON] # pass dict index
		nInsObjCursor.execute("DELETE FROM book where id=%s",n)
		self.nClsAttDB.commit()
		return {}	