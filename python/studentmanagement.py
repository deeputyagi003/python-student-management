students=[]
def add_student(): 
    name=input("Enter Student name:")
    roll=int(input("Enter roll number:"))
    marks=[]
    for i in range (5):
        m=int(input(f"Enter marks of subject {i+1}:"))
        marks.append(m)
    student={
        "name":name,
        "roll":roll,
        "marks":marks
    }
    students.append(student)
    print("Student added Successfully")
    
def view_student():
    if len(students)==0:
        print("No student found")
    else:
        for student in students :
            print("/n Name:", student["name"])
            print("/n Roll:",student["roll"])
            print("/n Marks:",student["marks"])
            print("-" * 20)
def calculate_total():
    roll=int(input("Enter roll number"))
    for student in students:
        if student["roll"]==roll:
            total=sum(student["marks"])
            print("total marks",total)
            return
        print("student not found")

def calculate_percentage():
    roll=int(input("enter roll number"))
    for student in students:
        if student["roll"]==roll:
            total=sum(student["marks"])
            percentage=(total/500)*100
            print("Percentage:",percentage,"%")
            return 

def highest_marks():
    if len(students)==0:
        print("No student found")
        return
    highest=max(students ,key=lambda s: sum(s["marks"]))
    print("Topper:",highest["name"])
    print("Total Marks",sum(highest["marks"]))

def search_student():
    roll=int(input("Enter roll number:"))
    for student in students:
        if student["roll"]==roll:
            print("Name:",student["name"])
            print("Roll:",student["roll"])
            print("Marks:",student["marks"])
            return
        print("Student not found")


def update_student():
    roll=int(input("Enter roll number:"))
    if roll in students:
        name=input("Enter new name:")
        marks=input("Enter new marks:")
        students[roll]["name"]=name
        students[roll]["marks"]=marks
        print("Student updates Successfully")    
    else:
        print("Student not found")

def delete_student():
    roll=int(input("Enter roll Number:"))
    if roll in students:
        del(students[roll])
        print("Student deleted Successfully")
    else:
        print("Student not found")
        
        
def main():
    while True:
        print("Student Management System")
        print("1.Add Student")
        print("2.View Student")
        print("3.Calculate Total")
        print("4.Calculate Percentage")    
        print("5.Highest Marks") 
        print("6.Search Student")      
        print("7.Update Student")   
        print("8.Delete Student")
        print("9.Exit")
        choice=int(input("Enter Your choice"))
        if choice==1:
            add_student()
        elif choice==2:
            view_student()
        elif choice==3:
            calculate_total()
        elif choice==4:
            calculate_percentage()
        elif choice==5:
            highest_marks()
        elif choice==6:
            search_student()
        elif choice==7:
            update_student()
        elif choice==8:
            delete_student()
        elif choice==9 :
            print("Thankyou")
            break
        else:
            print("Invalid choice")
main()

            
        