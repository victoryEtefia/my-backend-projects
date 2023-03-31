from flask import Flask
from flask import request
from random import randint
import Details
import bank
import mypin


app2=Flask("myserver")


@app2.post("/getbankdetails")
def getbankdetails():
    getbankdetails=bank.users
    index = randint(0,len(getbankdetails))
    return getbankdetails[index]
    
@app2.post("/names")
def names():
    names=Details.users
    return names

@app2.post("/register2")
def register2():



    responds={
        "success":False,
        "payload":{},
        "massage":"",
        "errors":[]
    }

    
    email=""
    firstname=""
    lastname=""
    middlename=""
    dateofbirth=""
    phonenumber=""
    address=""

    
    i=0
    hasfound=False
    try:
        email=request.form["email"]
        email=email.lower()
    except:
        responds="your email is not correct"
        return responds   
    try:
        firstname=request.form["firstname"]
        firstname=firstname.lower()
    except:
        error={
            "firstname":"missing field",
            "massage":"the firstname field is missing from the project"
        }
        responds['massage']="some error has occur"
        responds["errors"].append(error)
        return responds


    lastname=request.form["lastname"]
    lastname=lastname.lower()

    middlename=request.form["middlename"]
    middlename=middlename.lower()

    dateofbirth=request.form["dateofbirth"]

    phonenumber=request.form["phonenumber"]

    address=request.form["address"]
    address=address.lower()
    

    while(i<len(Details.users)):
        user=Details.users[i]
        if user["email"]==email:
         hasfound=True
        i=i+1


    
        

    if hasfound==True:
        responds="there is a user having this details"
        return responds
    else:
        newperson={
                "firstname":firstname,
                "lastname":lastname,
                "middlename":middlename,
                "dateofbirth":dateofbirth,
                "email":email,
                "phonenumber":phonenumber,
                "address":address,
        }
        Details.users.append(newperson)
        responds="your details has been registered successfully"
        return responds
    

