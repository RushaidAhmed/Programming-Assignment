def signin(user_name,password,file):
    files = open(file,"r")
    uname = files.readline().strip()
    pword = files.readline().strip()
    if user_name == uname and password == pword:
        return True
    else:
        return False