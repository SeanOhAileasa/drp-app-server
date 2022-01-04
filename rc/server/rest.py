from flask import Flask
app=Flask(import_name=__name__,static_url_path="",static_folder="../../rc/static/")

#
# https://web.archive.org/web/20220104195817/https://www.nytimes.com/books/best-sellers/
# January 4th, 2022
#
nBooks=[{"id":1,"Title":"THE JUDGE'S LIST","Author":"John Grisham","Price":29}, # type(nBooks[0]) # dict
    {"id":2,"Title":"THE STRANGER IN THE LIFEBOAT","Author":"Mitch Albom","Price":25},
    {"id":3,"Title":"IT ENDS WITH US","Author":"Colleen Hoover","Price":30}, # type(nBooks) # list
    {"id":4,"Title":"THE LINCOLN HIGHWAY","Author":"Amor Towles","Price":50},
    {"id":5,"Title":"CALL US WHAT WE CARRY","Author":"Amanda Gorman","Price":15}]
nNextID=4 # create new increment
# repository ./drp-app-server
@app.route(rule="/")
def fIndex():
    """URL map for "/" with method "GET".

Input: 
Process: 
Output: string
"""    
    return "Flask App - pythonanywhere"
# --- END ---
# repository ./drp-app-server
@app.route(rule="/books")
def fGetAll():
    """URL map for "/books" with method "GET".

Input: 
Process: (flask.jsonify) 
Output:
"""
    from flask import jsonify
    return jsonify(nBooks) # cURL: Content-Type: application/json
# --- END ---
# repository ./drp-app-server
@app.route(rule="/books/<int:nParID>")
def fFindById(nParID):
    """URL map for "/books/<int:nParID>" with method "GET".

Input: nParID
Process: create collection (convert to list); 
    filter parameters: i) lambda and; ii) actual collection
Output: if two books have same nParID then returns the first
"""
    from flask import jsonify
    nFound=list(filter(lambda n:n["id"]==nParID,nBooks))
    # print(type(nFound)) # cURL (refer server): <class 'list'>
    if len(nFound)==0: # test found nothing
        return jsonify({}),204 # return empty 204
    return jsonify(nFound[0]) # return first element
# --- END ---
# repository ./drp-app-server
@app.route(rule="/books",methods=["POST"])
def fCreate():
    """URL map for "/books" with method "POST".

Input: 
Process: (flask.request.json; flask.abort; flask.jsonify)
Output:
"""
    from flask import request,jsonify,abort
    global nNextID # new book id
    if not request.json: # request no json
        abort(400)
    nBook={"id":nNextID,
        "Title":request.json["Title"],
        "Author":request.json["Author"],
        "Price":request.json["Price"]} # create new book
    nBooks.append(nBook) # append new book
    nNextID+=1 # increment next new
    return jsonify(nBook) # return new book
# --- END ---
# repository ./drp-app-server
@app.route(rule="/books/<int:nParID>",methods=["PUT"])
def fUpdate(nParID):
    """URL map for "/books/<int:nParID>" with method "PUT".

Input: 
Process: (flask.request.json; flask.jsonify)
Output:
""" 
    from flask import jsonify,request
    nFound=list(filter(lambda n:n["id"]==nParID,nBooks))
    if len(nFound)==0: # test found nothing
        return jsonify({}),404 # return cannot find
    nCurrent=nFound[0] # current is found
    if "Title" in request.json:
        nCurrent["Title"]=request.json["Title"] # current new Title
    if "Author" in request.json:
        nCurrent["Author"]=request.json["Author"] # current new Author
    if "Price" in request.json:
        nCurrent["Price"]=request.json["Price"] # current new Price
    return jsonify(nCurrent) # return udpated book
# --- END ---
# repository ./drp-app-server
@app.route(rule="/books/<int:nParID>",methods=["DELETE"])
def fDelete(nParID):
    """URL map for "/books/<int:nParID>" with method "DELETE".

Input: 
Process: (flask.jsonify)
Output:
""" 
    from flask import jsonify
    nFound=list(filter(lambda n:n["id"]==nParID,nBooks))
    if len(nFound)==0: # test found nothing
        return jsonify({}),404 # return cannot find
    nBooks.remove(nFound[0]) # delete book found
    return jsonify({"done":True})
# --- END ---
if __name__=="__main__":
    app.run(debug=True)
