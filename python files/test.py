import string
ah=input("pleas input a word: ".title()).lower()
count={
    "a":0,
    "e":0,
    "i":0,
    "u":0,
}
if ah:
 for x in ah:
    if x in string.ascii_letters:
        if x in count:
         count[x]+=1
    elif x ==" ":
       pass    
    else:
        print(f"[{x}] is not a word")
 print(f"your word have:\n[A:{count["a"]}]\n[E:{count["e"]}]\n[I:{count["i"]}]\n[U:{count["u"]}]".title())        
else:
   print("pleas input.".title())