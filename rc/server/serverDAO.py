from flask import Flask
# from sys import path; path.insert(1,"../../") # original location "./DAO"
from DAO.bookDAO import CBookDAO # moved to "./rc/server/DAO" 

app=Flask(import_name=__name__,static_url_path="",static_folder="../../rc/static/")

@app.route(rule="/")
def fIndex():
    """URL map for "/" with method "GET".

Input: 
Process: (flask.redirect)
Output: redirection
"""  
    from flask import redirect
    return redirect("index.html")
    #
    # curl http://127.0.0.1:5000
    #
# --- END ---

@app.route(rule="/books")
def fGetAll():
    """URL map for "/books" with method "GET".

Input: 
Process: (flask.jsonify) 
Output:
"""
    from flask import jsonify
    nInsObjBook=CBookDAO() # instantiate object - CBookDAO
    return jsonify(nInsObjBook.fInsMetGetAllDict())
    #
    # curl http://127.0.0.1:5000/books
    #
# --- END ---

@app.route(rule="/books/<int:nParID>")
def fFindById(nParID):
    """URL map for "/books/<int:nParID>" with method "GET".

Input: nParID
Process: 
Output:
"""
    from flask import jsonify
    return jsonify(CBookDAO().fInsMetGetByID(nParID)) # instantiate object - CBookDAO
    #
    # curl http://127.0.0.1:5000/books/1
    #
# --- END ---

@app.route(rule="/books",methods=["POST"])
def fCreate():
    """URL map for "/books" with method "POST".

Input: 
Process: (flask.request.json; flask.abort; flask.jsonify)
Output:
"""
    from flask import request,jsonify,abort
    if not request.json: # request no json
        abort(400)
    nBook={"title":request.json["title"],
        "author":request.json["author"],
        "price":request.json["price"]}
    return jsonify(CBookDAO().fInsMetCreate(nBook)) # instantiate object - CBookDAO
    #
    # curl -X "POST" -d "{\"id\":10,\"title\":\"test title\",\"author\":\"test author\",\"price\":123}" -H Content-Type:application/json http://127.0.0.1:5000/books
    #
# --- END ---

@app.route(rule="/books/<int:nParID>",methods=["PUT"])
def fUpdate(nParID):
    """URL map for "/books/<int:nParID>" with method "PUT".

Input: 
Process: (flask.request.json; flask.jsonify)
Output:
""" 
    from flask import jsonify,request
    nFound=CBookDAO().fInsMetGetByID(nParID) # instantiate object - CBookDAO
    if len(nFound)=={}: # test found nothing
        return jsonify({}),404 # return cannot find
    nCurrent=nFound # current is found
    if "title" in request.json:
        nCurrent["title"]=request.json["title"] # current new title
    if "author" in request.json:
        nCurrent["author"]=request.json["author"] # current new author
    if "price" in request.json:
        nCurrent["price"]=request.json["price"] # current new price
    CBookDAO().fInsMetUpdate(nCurrent) # instantiate object - CBookDAO        
    return jsonify(nCurrent)
    #
    # curl -X "PUT" -d "{\"title\":\"testing title\",\"price\":999}" -H Content-Type:application/json http://127.0.0.1:5000/books/123
    #
# --- END ---

@app.route(rule="/books/<int:nParID>",methods=["DELETE"])
def fDelete(nParID):
    """URL map for "/books/<int:nParID>" with method "DELETE".

Input: 
Process: (flask.jsonify)
Output:
""" 
    CBookDAO().fInsMetDeleteTuple(nParID) # instantiate object - CBookDAO  
    from flask import jsonify
    return jsonify({"done":True})
    #
    # curl -X "DELETE" http://127.0.0.1:5000/books/123
    #
# --- END ---

if __name__=="__main__":
    app.run(debug=True)