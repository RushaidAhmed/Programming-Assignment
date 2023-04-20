from Authontication import *
files = open("student.txt","r")
username = input("enter your user name: ")
password = input("enter your password: ")
file ="userpassword.txt"

if signin(username,password,file)==True:
    print("student id","\t\t","student name","\t\t","student age","\t\t","student location",)
    for i in files:
        line=i.strip().split(":")
        print("\n"+line[0]+"\t\t\t\t\t"+line[1]+"\t\t\t\t"+line[2]+"\t\t\t\t"+line[3])
        
    x=open("student.txt","r")  
     
    name=[]
    age=[]
    for line in x:
        value=line.strip().split(":")
        name.append(value[1])
        age.append(int(value[2]))
    print("\n","No of students: ",len(name))
    print("Lowest age of student: ",min(age))
    print("Highest age of student: ",max(age))
    
else:
    print("Incorrect username and password")
    
      