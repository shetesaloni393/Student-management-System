class Student:
    def __init__(self,name,roll,passw,marks_1,marks_2):
        self.name=name
        self.roll=roll
        self.passw=passw
        self.marks_1=marks_1
        self.marks_2=marks_2

    @classmethod
    def acceptDetails(cls,name,roll,passw,marks_1,marks_2):
        ob=cls(name,roll,passw,marks_1,marks_2)
        l.append(ob)

    def displayTable(self,l):
        print("No.\tName\tRollno\tpassw\tMarks1\tMarks2")
        for i in range(l.__len__()):
            print(i+1,f"{l[i]. name}\t {l[i]. roll}\t {l[i]. passw}\t {l[i]. marks_1}\t{l[i]. marks_2}")

    def search(self,n):
        for i in range(l.__len__()):
            if n==l[i].roll:
                return i
    
    def displayDetails(self,d):
        print("Name:-",d.name)
        print("roll:-",d.roll)
        print("passw:-",d.passw)
        print("marks_1:-",d.marks_1)
        print("marks_2:-",d.marks_2)
        
    def update(self,rn,newroll):
        s=obj.search(rn)
        l[s].roll=newroll

    def delete(self,rn):
        s=obj.search(rn)
        del l[s]
    

l=[]
obj=Student("",0,0,0,0)
obj.acceptDetails("Saloni",1,'123',87,89)
obj.acceptDetails("Siddhi",2,'345',88,90)
obj.acceptDetails("Nivedita",3,'456',87,85)
obj.acceptDetails("Dhanashri",4,'789',82,84)



while True:
    print("1.Teacher Login\n2.student Login\n3.Log out")
    Login_choice=input("Enter your choice:-")
    if Login_choice=='1':
        TeachID='Teacher'
        Teachpass="1234"
        UserId=input("Enter User-Id:-")
        if UserId==TeachID:
            Userpass=input("Enter password:-")
            if Userpass==Teachpass:
                while True:
                    print("\n**********Teacher Login Successfull**********\n")
                    print("1.Accept student Details\n2.Display students Details\n3.Search students Details\n4.Update Students Details\n5.Delete Details\n6.Exit")
                    
                    ch=input("Enter your choice:-")
                    if ch=='1':
                        while True:
                            print("\n===Accept student Details===\n")
                            name=input("Enter name:-")

                            while True:
                                roll=input("Enter roll:-")
                                if roll.isdigit()==True:
                                    roll=int(roll)
                                    break
                                else:
                                    print("Invalid input..try again!")

                            while True:
                                marks_1=input("Enter marks:-")
                                if marks_1.isdigit()==True:
                                    marks_1=int(marks_1)
                                    break
                                else:
                                    print("invalid input..try again!")

                            while True:
                                marks_2=input("Enter marks:-")
                                if marks_2.isdigit()==True:
                                    marks_2=int(marks_2)
                                    break
                                else:
                                    print("invalid input..try again!")

                            
                            passw=input("Enter passw:-")

                            obj.acceptDetails(name,roll,passw,marks_1,marks_2)
                            
                        

                            for i in range(l.__len__()):
                                print("Name:-",l[i].name)
                                print("roll:-",l[i].roll)
                                print("marks_1:-",l[i].marks_1)
                                print("marks_2:-",l[i].marks_2)
                                print("passw:-",l[i].passw)
                                
                            print("\n1.Enter New Entry\n2.Exit\n")
                            ch=input("Enter your choice:-")
                            if ch=='1':
                                continue
                            else:
                                print("\nThank You!\n")
                                break

                    elif ch=='2':
                        while True:
                            print("\n=====Display Students Details=====\n")
                            print("====List of students====")
                        

                            obj.displayTable(l)

                            print("\n1.Do you want to see again\n2.Exit\n")
                            ch=input("Enter a choice:-")
                            if ch=='1':
                                continue
                            else:
                                break

                        
                    elif ch=='3':
                        while True:
                            print("\n======Search Students Details======\n")
                            n=input("Enter Roll Number:-")
                            if n.isdigit()==True:
                                n=int(n)
                                break
                            else:
                                print("Invalid input..try again!")

                        for i in range(l.__len__()):
                            if n==l[i].roll:
                                print("\n====Student Found====\n")
                                s=obj.search(n)
                                obj.displayDetails(l[s])


                    elif ch=='4':
                        while True:
                            print("\n=====Update Students Details=====\n")
                            rn=int(input("Enter Roll Number:-"))
                            newRoll=int(input("enter new roll number:-"))
                            obj.update(rn,newRoll)
                            
                            print("\n=====List after update=====\n")
                            obj.displayTable(l)

                            print("\n1.Do you want to see again\n2.Exit\n")
                            ch=input("Enter a choice:-")
                            if ch=='1':
                                continue
                            else:
                                break



                    elif ch=='5':
                        while True:

                            print("\n=====Delete Students Details=====\n")

                            rn=int(input("enter a roll no:-"))
                            obj.delete(rn)

                            print("\n====List after delete====\n")
                            obj.displayTable(l)

                            print("\n1.Do you want to delete again\n2.Exit\n")
                            ch=input("eneter your choice:-")
                            if ch==1:
                                continue
                            else:
                                break
                   

                    elif ch=='6':
                        print("\n===========Exit==========\n")
                        break
                    else:
                        print("\nInvalid input...try again!!\n")

            else:
                print("\nIncorrect password...try again!!\n")

        else:
            print(print("\nInvalid user ID...try again!!\n"))
    
    elif Login_choice=='2':
        while True:
            Stud_Id=input("\n Enter user-Id/Name:-")
            for i in range(l.__len__()):
                if l[i].name==Stud_Id:
                    Stud_pass=input("Enter your password:-")
                    for i in range(l.__len__()):
                        if l[i].passw==Stud_pass:

                            print("\n====",l[i].name,"you are login succesfull...!====\n")

                            rn=l[i].roll
                            s=obj.search(rn)
                            obj.displayDetails(l[s])
            print("\n1.Do you want to see again\n2.exit\n")
            ch=input("Enter your choice:-")
            if ch=='1':
                continue
            else:
                break
    elif Login_choice=='3':
        print("\nLog out====\n")
        break
    else:
        print("Invalid Input..Try again...!!")                



                    


            

