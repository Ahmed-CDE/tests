import string
file=open(r"D:\important text\student.text", "a")
file=open(r"D:\important text\student.text", "r")
Pre_existing_data=file.read()
student_information={

}
def student_names():
 student_information
 def student_names(**d):
     table_list=[]
     for x, z in d.items():
         table_list.append(x)
     return table_list
 return student_names(**student_information) 
marks_list=[]
the_finch_loop=""
def marks(marks_list):
    from string import digits
    marks=[]
    def mark(mark_str):
        z=""
        for x in mark_str:
            if x in digits:
                z+=x
            elif x not in digits:
                pass   
        return z    
    for n in range(0,len(marks_list)):
        marks.append(int(mark(marks_list[n])))
    return marks
if Pre_existing_data:
    print(f"{"#####this is a data in the file#####\n".title()}{Pre_existing_data}")
    information_in_file=file.readlines()
    for x in information_in_file:
       x=x.split(":")
       student_information[x[0]]=x[1]
else:
  file=open(r"D:\important text\student.text", "a")
  student_name=input("pleas input a student: ".title()).strip()
  student_marks_list_str=input("pleas input a student marks: ".title()).strip().split()
  student_information[student_name]=marks(student_marks_list_str)
the_finish_loop=""
while the_finch_loop!="yes" or the_finch_loop!="y":
   the_finch_loop=input("do you want to exit now (yes or no): ".title()).lower().strip()
   if the_finch_loop=="yes" or the_finch_loop=="y":
      break
   response=input("pleas choose what do you wand to do [delete or add or edit]: ".title()).lower().strip()
   if response=="add" or response=="a":
       student_name=input("pleas input a student: ".title()).strip()
       def student_add(student_name_1):
        if student_name_1 in student_names():
            student_name_1=input("this name is already in the list pleas input another name: ".title()).strip()
            return student_add(student_name_1)
        else:
            student_name_1
            return student_name_1
       student_name=student_add(student_name)
       student_marks_list_str=input("pleas input a student marks: ".title()).strip().split()
       student_information[student_name]=marks(student_marks_list_str)
       print("complete add a studentL".title())
   elif response=="delete" or response=="d":
      student_name=input("pleas input a student: ".title()).strip()
      def student_delete(student_name_1):
        if student_name_1 not in student_names():
            student_name_1=input("this name is not in the list pleas input another name: ".title()).strip()
            return student_delete(student_name_1)
        else:
            student_name_1
            return student_name_1
      student_name=student_delete(student_name)
      student_information.pop(student_name)
      print("complete delete a student".title())
   elif response=="edit"or response=="e":
      student_name=input("pleas input a student: ".title()).strip()
      def student_delete(student_name_1):
        if student_name_1 not in student_names():
            student_name_1=input("this name is not in the list pleas input another name: ".title()).strip()
            return student_delete(student_name_1)
        else:
            student_name_1
            return student_name_1
      student_name=student_delete(student_name)
      print(f"the is data of student before edit {student_name}:{student_information[student_name]}")
      while the_finish_loop!="no" or the_finish_loop!="n":
         choose=input("pleas choose what do you want to edit (name or marks): ".title()).strip().lower()
         if choose=="marks" or choose=="mark" or choose=="m":
            the_num_mark=int(input("pleas input a number of mark you want to change it".title()).strip())-1
            new_mark=int(input("pleas input a new mark".title()).strip())
            student_information[student_name][the_num_mark]=new_mark
         elif choose=="name" or choose=="n":
              new_name=input("pleas input anew name".title()).strip()
              student_information[new_name]=student_information[student_name]
              student_information.pop(student_name)
         else: 
            print(f"you choice [{choose}]. pleas choice from [name or mark]".title()) 
   else:
        print(f"you choice [{response}]. pleas choice from [delete or add or edit]".title())
for x, z in student_information.items():
    file=open(r"D:\important text\student.text", "a")
    file.write(f"{x}:{z}\n")