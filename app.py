from random import randint
from flask import Flask
from flask import request
import db
import checker


app=Flask(__name__)

app=Flask("myserver")


@app.get("/myhome")
def myhome():
    return "i am sending you home"



@app.post("/guessnumber")
def guessnumber():
    responds={
        'success':False,
        'payload':{},
        'massage':"",
        "errors":[]
    }
    try:
        fromuser=int(request.form["num"])
        think= randint(5,20)

        responds['payload']={
            "random number":think,
            "guessed number":fromuser
        }
        
        if (fromuser)>(think):
            responds['massage']= "your guess is greater"
            return responds
        elif (fromuser==think):
            responds["massage"]=True
            responds['success'] ="woooow your guess is correct"
            return responds 
        else:
            responds['massage']= "your guess is incorrect"
            return responds
    except:
        responds['success]']=False
        responds['payload']={}
        responds ["massage"]="the was an exception in the error"

        error ={
            "error type":"missing field",
            "error massage":"the num field is missing"
        }
        responds['errors'].append(error)

        return responds

@app.post("/getusers")
def getusers():
    getusers=db.users
    return getusers


@app.post("/register")
def register():
    
    responds={
        'success':False,
        'payload':{},
        'massage':"",
        'errors':[]
        }

    email=""
    password=""
    age=""
    name=""

    try:
        email=str(request.form["email"])
        email=email.strip().lower()   
    except:
        error1={
            'name':"missing field",
            'massage':"the email field is missing from the project"
        }
        responds['massage']='some error has occur'
        responds['errors'].append(error1)
        
    try:
        password=request.form["password"]
    except:
        error1={
            'name':"missing field",
            'massge':"the password field is missing"
        }
        responds['massage']="some error has occur"
        responds['errors'].append(error1)
    try:
      age=request.form["age"]
    except:
        error1={
            'name':"missing field",
            'massage':"the age field is missing from the project"
        }
        responds['massage']='some error has occur'
        responds['errors'].append(error1)
        

    try:
      name=request.form["name"]
    except:
        error1={
            'name':"missing field",
            'massage':'the name field is missing from the project'
        }
        responds['massage']='some errors has occur'
        responds['errors'].append(error1)

    lenofpassword=len(password)
    if lenofpassword<=7:
        err={
            'name':"weak password",
            'massage':"the password must be more than 8 characters"
        }
        responds["massage"]="they are some errors check very well"
        responds['errors'].append(err)
        

    check=checker.passwordValidator(password)
    if check !=True:
        err={
            'name':" weak password",
            'massage':check
        }
        responds["massage"]="there is some error, check the errors property "
        responds["errors"].append(err)

    num_of_errors=len(responds['errors'])
    if num_of_errors>0:
        return responds


    newperson={
        'email':email,
        "password":password,
        "age":age,
        "name":name
    
    }

    
    i=0
    hasfound=False
    while(i<len(db.users)):
        user=db.users[i]
        if user["email"]==email:
            hasfound=True
        i=i+1

    if hasfound==True:
        err={
            'name':"email existing",
            "massage":f"there is a user having this email({email}))"

        }
        responds['errors'].append(err)
        responds['massage']=f'the email address you entered already exist..({email})'
        return responds
    else:
        db.users.append(newperson)
        
        responds['success']=True
        responds['payload']=newperson
        responds['massage']="your account has been registered successfully"
        return (responds)
        # return "correct"

@app.post("/login")
def login():
    users=db.users


    responds={
            'success':False,
            'payload':{},
            'massage':"",
            "errors" :[]
        }
    try:
        email=request.form["email"]
    except:
        error1={
            'name':'missing email field',
            'massage':"please provide a password for the login"
        }
        responds["errors"].append(error1)

    try:
        checker=request.form['password']
    except:
        error2={
            'name':'missing password field',
            'massage':"please provide a password for the login"
        }
        responds['errors'].append(error2)

    if(len(responds['errors'])>0):
        responds['massage']="there was some errors,please check the errors property"
    else:
        i=0
        while(i<len(db.users)):
            person=db.users[i]
            if (str(person["email"]).lower()==str(email).lower() and person ["password"]==checker):
                responds['massage']="login was successful"
                responds["success"]=True
                responds['payload']=person
            i=i+1
        if (responds['success']==False):
            responds['massage']="email or password is not valid"
        

    return responds
