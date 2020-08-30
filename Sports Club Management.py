#use _author_ = 'Kuruvilla 
import pickle
from _projectmodules import project 
ch=1
while ch!=0:
    print("(1) Access Member File")
    print("(2) Access Fees File")
    print("(3) Access Facility File")
    print("(4) Display Records")
    print("(0) Exit Menu")
    ch=int(input("Enter Choice"))
    if ch==1:
        while ch!=0:
            print("(1) Input New Member details")
            print("(2) Search for Member details")
            print("(3) Edit Member details")
            print("(4) Delete Member Records")
            print("(0) Exit Menu")
            ch=int(input("Enter Choice"))
            if ch==1:
                project.newmember()
            elif ch==2:
                project.searchmember()
            elif ch==3:
                project.editdetails()
            elif ch==4:
                project.deleterec()
        ch=1
    elif ch==2:
        while ch!=0:
            print("(1) Display Fees File")
            print("(2) Update Fees File")
            print("(0) Exit Menu")
            ch=int(input("Enter Choice"))
            if ch==1:
                project.dispfees()
            elif ch==2:
                project.updatefees()
        ch=2
    elif ch==3:
        while ch!=0:
            print("(1) Add new facilites")
            print("(0) Exit Menu")
            ch=int(input("Enter Choice"))
            if ch==1:
                project.addfac()
        ch=3
    elif ch==4:
        while ch!=0:
            print("(1) Display All Member Records")
            print("(2) Display Facilites Available")
            print("(3) Members Fees due in Month")
            print("(0) Exit Program")
            ch=int(input("Enter Choice"))
            if ch==1:
                project.display()
                with open("Member File.dat",'rb') as f5:
                    try:
                        list1=[]
                        while True:
                            rec=pickle.load(f5)
                            list1.append(rec)
                    except:
                        list2=['Code','Name','Date','Address','Phone','F1','F2','F3']
                        print("{:<10} {:<16} {:<12} {:<22} {:<10} {:<3} {:<3} {:<3}".format(list2[0],list2[1],list2[2],list2[3],list2[4],list2[5],list2[6],list2[7]))
                        for k in list1:
                            print("{:<10} {:<16} {:<12} {:<22} {:<10} {:<3} {:<3} {:<3}".format(k[0],k[1],str(k[2]),k[3],k[4],k[5],k[6],k[7]))
                

            elif ch==2:
                project.dispfac()
            elif ch==3:
                project.duefees()
        ch=4
                

        



                
        

                    

