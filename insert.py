from Authontication import *
files=open("student.txt","a")
username=input("enter your user name: ")
password=input("enter your password: ")
file="userpassword.txt"
if signin(username,password,file)==True:
    while True:
        s_id=input("Enter your student id or exit: ")
        if s_id=="exit":
            break
        else:
            s_name=input("Enter your student name: ")
            s_age=input("Enter your student age: ")
            s_location=input("Enter your student location: ") 
            details=(s_id+":"+s_name+":"+s_age+":"+s_location+"\n")
        files.write(details)
else:
    print("Password incorrect")