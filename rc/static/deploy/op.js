host=window.location.origin // ajax calls http://127.0.0.1:5000
function fAddBookToTable(nParObjBookJS)
{
    var nTableElement=document.getElementById("tableBook"); // DOM object HTMLTableElement
    var nRowElement=nTableElement.insertRow(-1); // DOM object HTMLTableRowElement
    nRowElement.setAttribute("id",nParObjBookJS.id); // add attribute value

    var nCell1=nRowElement.insertCell(0); // DOM HTMLTableRowElement [0]
    nCell1.innerHTML=nParObjBookJS.id; // DOM add id

    var nCell2=nRowElement.insertCell(1); // DOM HTMLTableRowElement [1]
    nCell2.innerHTML=nParObjBookJS.title; // DOM add title

    var nCell3=nRowElement.insertCell(2); // DOM HTMLTableRowElement [2]
    nCell3.innerHTML=nParObjBookJS.author; // DOM add author

    var nCell4=nRowElement.insertCell(3); // DOM HTMLTableRowElement [3]
    nCell4.innerHTML=nParObjBookJS.price; // DOM add price

    var nCell5ButtonUpdate=nRowElement.insertCell(4); // DOM HTMLTableRowElement [4]
    nCell5ButtonUpdate.innerHTML="<button onclick=\"fShowUpdate(this)\">Update</button>"; // DOM add button

    var nCell6ButtonDelete=nRowElement.insertCell(5); // DOM HTMLTableRowElement [5]
    nCell6ButtonDelete.innerHTML="<button onclick=\"fDoDelete(this)\">Delete</button>"; // DOM add button
}
function fPopulateTable()
{
    // const nObjBookJS={"id":2,"title":"Learning Python","author":"Mark Lutz","price":3000} // testing purposes only
    // fAddBookToTable(nObjBookJS) // testing purposes only
    $.ajax({
        "url":host+"/books", // ajax call fGetAll
        "method":"GET",
        "dataType":"JSON",
        "success":function(nParCollectionJSON)
        {
            for (nEachBook of nParCollectionJSON) // iterate JSON collection
                fAddBookToTable(nEachBook) // populate object HTMLTableElement
        },
        "error":function(xhr,status,error)
        {
            console.log("error: "+status+" msg:"+error);
        }                    
    });
    console.log("host... "+host);
}

fPopulateTable()     

function fClearCreateUpdate()
{
    var nFormCreateUpdate=document.getElementById("tableCreateUpdate"); // parent work down
    nFormCreateUpdate.querySelector("input[name=\"title\"]").value=""; // search child elements
    nFormCreateUpdate.querySelector("input[name=\"author\"]").value="";
    nFormCreateUpdate.querySelector("input[name=\"price\"]").value="";
}
function fShowCreateUpdate()
{
    document.getElementById("divTableBook").style.display="none";          
    document.getElementById("divCreateUpdate").style.display="block";
    document.getElementById("buttonUpdate").style.display="none"; 
    document.getElementById("buttonCreate").style.display="block";
    fClearCreateUpdate()
}
function fGetBookFromCreateUpdate()
{
    var nFormCreateUpdate=document.getElementById("tableCreateUpdate"); // parent work down
    const nObjBookJS={}; // JS object Object
    nObjBookJS.title=nFormCreateUpdate.querySelector("input[name=\"title\"]").value; // search child elements
    nObjBookJS.author=nFormCreateUpdate.querySelector("input[name=\"author\"]").value;
    nObjBookJS.price=nFormCreateUpdate.querySelector("input[name=\"price\"]").value;
    // console.log("via name: "+nObjBookJS.title+","+nObjBookJS.author+","+nObjBookJS.price); // access via name
    // let n=""; for (let nEachProperty in nObjBookJS){n+=nObjBookJS[nEachProperty]+",";}; console.log("via loop: "+n); // access via loop      
    // console.log("via array: "+Object.values(nObjBookJS)); // convert to array
    // console.log("via string: "+JSON.stringify(nObjBookJS)); // convert to string 
    return nObjBookJS;
}
function fShowTableBook()
{
    document.getElementById("divCreateUpdate").style.display="none";
    document.getElementById("divTableBook").style.display="block";
} 
function fDoCreate()
{
    let nObjBookJS=fGetBookFromCreateUpdate(); // JS object Object
    // console.log("nObjBookJS: "+JSON.stringify(nObjBookJS)); // string names x3
    $.ajax({
        "url":host+"/books", // ajax call fCreate
        "method":"POST",
        "data":JSON.stringify(nObjBookJS),
        "dataType":"JSON",
        contentType:"application/json; charset=utf-8",
        "success":function(nParAutoIncrementID)
        {
            nObjBookJS.id=nParAutoIncrementID; // add name id   
            // console.log("nObjBookJS: "+JSON.stringify(nObjBookJS)); // string names x4
            fAddBookToTable(nObjBookJS)
            fClearCreateUpdate()
            fShowTableBook()
        },
        "error":function(xhr,status,error)
        {
            console.log("error: "+status+" msg:"+error);
        }                    
    });   
}
function fReadRowFromTable(nParRowElement)
{
    const nObjBookJS={}; // JS object Object
    nObjBookJS.id=nParRowElement.getAttribute("id"); // grab attribute id
    nObjBookJS.title=nParRowElement.cells[1].firstChild.textContent;
    nObjBookJS.author=nParRowElement.cells[2].firstChild.textContent;
    nObjBookJS.price=nParRowElement.cells[3].firstChild.textContent;
    return nObjBookJS
}
function fPopulateForm(nParObjBookJS)
{
    var nFormCreateUpdate=document.getElementById("tableCreateUpdate"); // parent work down
    nFormCreateUpdate.querySelector("input[name=\"id\"]").value=nParObjBookJS.id; // search child elements
    nFormCreateUpdate.querySelector("input[name=\"title\"]").value=nParObjBookJS.title;
    nFormCreateUpdate.querySelector("input[name=\"author\"]").value=nParObjBookJS.author;
    nFormCreateUpdate.querySelector("input[name=\"price\"]").value=nParObjBookJS.price;
}
function fShowUpdate(nParThis)
{
    var nRowElement=nParThis.parentNode.parentNode; // parent work up
    fPopulateForm(fReadRowFromTable(nRowElement));
    document.getElementById("divTableBook").style.display="none";
    document.getElementById("divCreateUpdate").style.display="block";
    document.getElementById("buttonCreate").style.display="none";    
    document.getElementById("buttonUpdate").style.display="block";              
}
function fUpdateRowCreateUpdate(nParObjBookJS)
{
    var nRowElement=document.getElementById(nParObjBookJS.id);
    nRowElement.cells[1].firstChild.textContent=nParObjBookJS.title;
    nRowElement.cells[2].firstChild.textContent=nParObjBookJS.author;
    nRowElement.cells[3].firstChild.textContent=nParObjBookJS.price;
} 
function fUpdateServer(nParObjBookJS)
{
    // console.log("nParObjBookJS: "+JSON.stringify(nParObjBookJS)); // string names x3
    var nFormCreateUpdate=document.getElementById("tableCreateUpdate"); // parent work down
    nParObjBookJS.id=nFormCreateUpdate.querySelector("input[name=\"id\"]").value; // add name id
    // console.log("nParObjBookJS: "+JSON.stringify(nParObjBookJS)); // string names x4
    $.ajax({
        "url":host+"/books/"+nParObjBookJS.id, // ajax call fUpdate
        "method":"PUT",
        "data":JSON.stringify(nParObjBookJS),
        "dataType":"JSON",
        contentType:"application/json; charset=utf-8",
        "success":function(nParObjBookJS)
        {                    
            fUpdateRowCreateUpdate(nParObjBookJS)
            fShowTableBook()
            fClearCreateUpdate()
        },
        "error":function(xhr,status,error)
        {
            console.log("error: "+status+" msg:"+error);
        }                    
    });               
}
function fDoUpdate()
{
    fUpdateServer(fGetBookFromCreateUpdate())
}          
function fDoDelete(nParThis)
{
    var nTableElement=document.getElementById("tableBook");
    var nRowElement=nParThis.parentNode.parentNode;
    var nRemoveIndex=nRowElement.rowIndex;
    var nID=nRowElement.getAttribute("id");
    $.ajax({
        "url":host+"/books/"+nID, // ajax call fDelete
        "method":"DELETE",
        "data":"",
        "dataType":"JSON",
        "success":function(nParObjBookJSEmpty)
        {
            nTableElement.deleteRow(nRemoveIndex); // delete row index
        },
        "error":function(xhr,nParStatus,nParError)
        {
            console.log("error: "+nParStatus+"msg: "+nParError);
        }
    });
}