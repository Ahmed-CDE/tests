file=open(r"D:\important text\student.text", "w")
file.write("Ahmed:[100, 100, 50000]")
file=open(r"D:\important text\student.text", "r")
student_list=[]

print(file.read())
file.seek(0)
file_readlines=file.readlines()
print(file_readlines)
for x in file_readlines:
    z="".join(x)
    z=z.split(":")
    name=z[0]
    mark=z[1]
    print(mark, name)

