import string
theinformationsofstudints={

}
the_answer=""
while the_answer!="no": 
   marks_int_list=[] 
   name=input("pleas input a student name: ".title()).strip()
   marks_str_list=input("pleas input a student marks: ".title()).strip().split()
   if marks_str_list:
      if len(marks_str_list)==3:
       for x in marks_str_list:
         for z in x:
            if z in string.ascii_letters or z in string.punctuation:
               n=marks_str_list.index(x)
               marks_str_list[n]=x.replace(z, "")
       for x in marks_str_list:
        marks_int_list.append(int(x))
       the_answer=input("if you dont need add a nothre student just write (no): ".title()).lower()     
      else:
        print(f"pleas add a [3] marks you add a {[len(marks_str_list)]}".title())
        the_answer=input("pleas add a student: ".title()).lower()
   marks_int_list.sort()
   theinformationsofstudints[name]={
     "marks":marks_int_list,
   }
   avreg=sum(theinformationsofstudints[name]["marks"])/3
   theinformationsofstudints[name]["avreg"]=avreg
   if avreg>=60:
     result="pass"
     theinformationsofstudints[name]["result"]=result
   else:
     result="fail"  
   theinformationsofstudints[name]["result"]=result
for x in theinformationsofstudints:
 print(f"student: {x}\nmarks: {theinformationsofstudints[x]["marks"]}\nthe avreg: {theinformationsofstudints[x]["avreg"]}".title())
 print("="*50)