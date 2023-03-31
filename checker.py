import string

password="2468aerJF@!#"

def passwordValidator(password):

        listofsmall=list(string.ascii_lowercase)
        listofupper=list(string.ascii_uppercase)
        listofspecial=list(string.punctuation)
        listofdigit=list(string.digits)

        missing_criteria="your password is missing...."

        smallflag=False
        i=0
        while i<len(listofsmall):
            alp=listofsmall[i]
            if password.find(alp)>=0:
                smallflag=True
                break
            i=i+1
        if smallflag==False:    
         missing_criteria=missing_criteria +" small character..."



        upperflag=False
        y=0
        while y<len(listofupper):
            alp=listofupper[y]
            if password.find(alp)>=0:
                upperflag=True
                break
            y=y+1
        if upperflag==False:
            missing_criteria=missing_criteria +" upper character.."    


        specialflag=False
        z=0
        while z<len(listofspecial):
            alp=listofspecial[z]
            if password.find(alp)>=0:
                specialflag=True
                break
            z=z+1
        if specialflag==False:
            missing_criteria=missing_criteria +" special character.."    


        digitflag=False
        d=0
        while d<len(listofdigit):
            alp=listofdigit[d]
            if password.find(alp)>=0:
                digitflag=True
                break
            d=d+1
        if digitflag==False:
            missing_criteria=missing_criteria +" digit character..."


        if smallflag==True and upperflag==True and specialflag==True and digitflag==True:
            return True
        else:
            return(missing_criteria) 
                

check=passwordValidator("1267@#agjEJIK")  


print(check)
                