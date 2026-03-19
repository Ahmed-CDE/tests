import re
class Student:
    z=[]
    num_of_student=0
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
        Student.num_of_student+=1
    def add_marks(self, new_mark):
          self.marks=self.marks.append(new_mark)
          return Student.z
    def result(self):
        if self.average()>=50:
            return "you pass".title()
        else:
            return "you failed".title()
    def average(self):
       return sum(self.marks)/len(self.marks)
exit_loop=None
v_name=[]
while exit_loop!="y" and exit_loop!="yes":
 Student_name=input("pleas input a name: ".title()).strip()
 Student_marks_1=input("pleas input a marks: ".title()).strip()
 Student_marks_1=re.split(r",+|\s+|,\s+", Student_marks_1)
 Student_marks=[]
 for x in Student_marks_1:
     if x:
      Student_marks.append(int(x))
 Student_name=Student(Student_name, Student_marks)
 add=input("do you want add a mark [yes or no]: ".title()).lower()
 if add=="y" or add=="yes":
  Student_add=int(input("pleas add a number: ".title()).strip())
  Student_name.add_marks(Student_add)
 v_name.append(Student_name)
 exit_loop=input("do you want exit: ".title()).strip().lower()
print("DATA".center(50, "="))
for x in v_name:
    print(f"student[{x.name}]\nmarks:{x.marks}\nthe average:{x.average()}\nthe student is:{x.result()}\n{"="*50}".title())