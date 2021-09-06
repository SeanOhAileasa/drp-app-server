from flask import Flask
app=Flask(import_name=__name__,static_url_path="",static_folder="../../rc/static/")
# repository ./drp-app-server
@app.route(rule="/")
def fIndex():
    """URL map for "/" with method "GET".

Input: 
Process: 
Output: string
"""    
    return "Flask App - pythonanywhere"
    #
    # curl http://127.0.0.1:5000
    #
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
    return jsonify({})
    #
    # curl http://127.0.0.1:5000/books
    #
# --- END ---
# repository ./drp-app-server
@app.route(rule="/books/<int:nParID>")
def fFindById(nParID):
    """URL map for "/books/<int:nParID>" with method "GET".

Input: nParID
Process: 
Output:
"""
    from flask import jsonify
    return jsonify({})
    #
    # curl http://127.0.0.1:5000/books/1
    #
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
    if not request.json: # request no json
        abort(400)
    nBook={"id":request.json["id"],
        "title":request.json["title"],
        "author":request.json["author"],
        "price":request.json["price"]}
    return jsonify({})
    #
    # curl -X "POST" -d "{\"id\":10,\"title\":\"test title\",\"author\":\"test author\",\"price\":123}" -H Content-Type:application/json http://127.0.0.1:5000/books
    #
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
    nFound=[]
    if len(nFound)==0: # test found nothing
        return jsonify({}),404 # return cannot find
    nCurrent=nFound[0] # current is found
    if "title" in request.json:
        nCurrent["title"]=request.json["title"] # current new title
    if "author" in request.json:
        nCurrent["author"]=request.json["author"] # current new author
    if "price" in request.json:
        nCurrent["price"]=request.json["price"] # current new price
    return jsonify(nCurrent)
    #
    # curl -X "PUT" -d "{\"title\":\"testing title\",\"price\":999}" -H Content-Type:application/json http://127.0.0.1:5000/books/123
    #
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
    return jsonify({"done":True})
    #
    # curl -X "DELETE" http://127.0.0.1:5000/books/123
    #
# --- END ---
if __name__=="__main__":
    app.run(debug=True)
