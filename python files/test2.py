import string
subjects_list= list(input("pleas add a subject to your list: ".title()))
for x in subjects_list:
    if x in string.punctuation:
        subjects_list.remove(x)
subjects_str="".join(subjects_list)
subjects_list=subjects_str.split()
addsubjects=""
deletsubjects=""
while addsubjects!="no" :
    addsubjects=input("do you want add anew subjects(yes or no): ".title()).lower()
    if addsubjects=="yes":
        newsubjects=input("add a new subjects:".title())
        subjects_list.append(newsubjects)
    elif addsubjects!="no":
        print("pleas input yes or no just.".title())    
print(f"this is your list {subjects_list}".title())        
while deletsubjects!="no":
    deletsubjects=input("do you want delet object yes or no: ".title()).lower()
    if deletsubjects=="yes":
        deletobject=input("what do you want delet: ".title())
        if deletobject in subjects_list:
            subjects_list.remove(deletobject)
        else:
            print("pleas input a subject in you list.".title())    
    elif deletsubjects!="no":
        print("pleas input yes or no just.".title())
print(f"this is you list {subjects_list}") 
print(f"this is the numper of supjects in your list [{len(subjects_list)}]".title()) 
subjects_tuple=tuple(subjects_list)
print(subjects_tuple)      