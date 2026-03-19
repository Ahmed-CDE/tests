import string
name=input("pleas input your name: ".title())
age=(input("pleas input your age: ".title()))
cuntre=input("pleas input yout cuntre name: ".title())
youser_information_name_list=[]
youser_information_age_list=[]
youser_information_cuntre_list=[]
for x in name:
    if x in string.ascii_letters:
        youser_information_name_list.append(x)
    else:
        print(f"sorry the {x} is not word i will remove it".title())
for x in age:
    if x in string.digits:
        youser_information_age_list.append(x)
    else:
        print(f"sorry the {x} is not a numper i will remove it".title())
for x in cuntre:
    if x in string.ascii_letters:
        youser_information_cuntre_list.append(x)
    else:
        print(f"sorry the {x} is not word i will remove it".title())  
youser_information_name="".join(youser_information_name_list)
youser_information_age="".join(youser_information_age_list)
youser_information_cuntre="".join(youser_information_cuntre_list)         
print(f"{"ID CARD".center(27,"=")}\nname: {youser_information_name}\nage: \
{youser_information_age}\ncountre: {youser_information_cuntre}\n{"="*27}".title())