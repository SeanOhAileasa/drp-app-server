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
    return "Flask App"
# --- END ---
# repository ./drp-app-server
@app.route(rule="/books")
def fGetAll():
    """URL map for "/books" with method "GET".

Input: 
Process: 
Output:
"""    
    return "ACTION: Get all"
# --- END ---
# repository ./drp-app-server
@app.route(rule="/books/<int:nParID>")
def fFindById(nParID):
    """URL map for "/books/<int:nParID>" with method "GET".

Input: 
Process: 
Output:
"""    
    return "ACTION: Find by id ("+str(nParID)+")"
# --- END ---
# repository ./drp-app-server
@app.route(rule="/books",methods=["POST"])
def fCreate():
    """URL map for "/books" with method "POST".

Input: 
Process: later take the json passed 
Output:
"""    
    return "ACTION: Create"
# --- END ---
# repository ./drp-app-server
@app.route(rule="/books/<int:nParID>",methods=["PUT"])
def fUpdate(nParID):
    """URL map for "/books/<int:nParID>" with method "PUT".

Input: 
Process: 
Output:
"""    
    return "ACTION: Update ("+str(nParID)+")"
# --- END ---
# repository ./drp-app-server
@app.route(rule="/books/<int:nParID>",methods=["DELETE"])
def fDelete(nParID):
    """URL map for "/books/<int:nParID>" with method "DELETE".

Input: 
Process: 
Output:
"""    
    return "ACTION: Delete ("+str(nParID)+")"
# --- END ---
if __name__=="__main__":
    app.run(debug=True)
