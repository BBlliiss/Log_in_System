
users={};

def CheckForInput(_text):
    while 1:
        content=input(_text)
        if not content or " " in content:
            print("Input error")
        else:
            return content
    
while 1:
    option=input("log in(1) or register(2):")
    
    if(option=="1"):
        logInName=CheckForInput("Please enter your username:")
        logInPassword=CheckForInput("Please enter your password:")
        
        if not users.get(logInName):
            print("The name does not exist")
            
        elif users[logInName]["accountState"]=="Frozen":
            print("The account is frozen,please contact administrator")
            
        else:
            if users[logInName]["password"]==logInPassword:
                users[logInName]["typeChances"]=3
                print("Log in successfully")
                
                choice=input("back(1) or logout(2) or exit(others):")
                
                if choice=="1":
                    pass
                
                elif choice=="2":
                    del users[logInName]
                    print("Logout successfully")
                    
                else:
                    break
                
            else:
                users[logInName]["typeChances"]-=1
                print("Password error") 
                if(users[logInName]["typeChances"]==0):
                    users[logInName]["accountState"]="Frozen"
                    print("The password was wrong too many times and the account was frozen")

    elif(option=="2"):
    
        registerName=CheckForInput("Please enter your register name:")
        registerPassword=CheckForInput("Please enter your password:")
    
        if users.get(registerName):
            print("The name already exists")
            
        else:
            users.update({registerName:{"password":registerPassword,"typeChances":3,"accountState":"Normal"}})
            print("Register successfully")
            
    else:
        break
