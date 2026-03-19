# file=open(r"D:\important text\test.text", "w")
# file.write("this is a text to test a functions in python\n".title())
# file=open(r"D:\important text\test.text", "a")
# file.write("this is a new line".title())
# file=open(r"D:\important text\test.text", "r")
# print(file.read(10000))
# # file=open(r"D:\important text\test.text", "a")
# # file.truncate(5)
# print(file.tell())
# file.seek(8)
# print(file.readlines())
# print(file.readline())
# # #import os
# # #os.remove(r"D:\important text\test.text")
# -----------------------------------------------------------------------

# list_test=[2, 8, 4]
# # if all(n%2==0 for n in list_test):
# #     print("all of the item is zwge")
# # else:
# #     print("there a item is not a zwge")
# if any(n%2==0 for n in list_test):
#     print("there a item is zwge in a list")
# else:
#     print("not there any item zwgi in the list")
# print(bin(1))
# a=1
# b=2
# print(id(a))
# -----------------------------------------------------------------------

# def myname(name):
#     return f"-{name}-"
# list_name=["ahmed", "mohamed", "magdy"]
# address=map(myname, list_name)
# print(address)
# for x in address:
#     print(x)
# -----------------------------------------------------------------------

# reversed()
# مثال
# name="ahmed"
# print(reversed(name))
# for litter in reversed(name):
#     print(litter)
# list_test=["ahmed", "python", "html", "c++", 100]    
# for items in reversed(list_test):
#     print(items)
# -----------------------------------------------------------------------

# # import test5
# # test5.hello("ahmed")
# # test5.how_are_you("ahmed")
# import test5 as ee
# ee.hello("ahmed")
# ee.how_are_you("ahmed")
# -----------------------------------------------------------------------

# list_test_int=[1, 2, 3, 4]
# list_test_name=["ahmed\n","magdy\n","atalla\n"]
# print(*list_test_name)
# import termcolor
# import pyfiglet
# file.write(termcolor.colored(pyfiglet.figlet_format("Ahmed"), color="white"))
# print(termcolor.colored(pyfiglet.figlet_format("Ahmed"), color="white"))
# -----------------------------------------------------------------------

# import datetime
# print(dir(datetime))
# print(dir(datetime.datetime))
# print(datetime.datetime.now())
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().day)
# print(datetime.datetime.min)
# print(datetime.datetime.max)
# print(datetime.datetime.now().time())
# print(datetime.time().min)
# print(datetime.time().max)
# print(datetime.datetime(2009, 11, 25))
# print(datetime.datetime(2009, 11, 25, 4, 25, 45, 354452))
# import time
# -----------------------------------------------------------------------

import termcolor
import pyfiglet
print(termcolor.colored((pyfiglet.figlet_format(("game over".title()))), color="red"))
print(termcolor.colored((pyfiglet.figlet_format(("game over".upper()))), color="red"))
# -----------------------------------------------------------------------

# from PIL import Image
# my_image=Image.open(r"C:\Users\Ahmed\Pictures\png folder\static.png")
# my_image.show()
# mybox=(0, 0, 400, 400)
# my_image=my_image.crop(mybox)
# my_image.show()
# my_convert=my_image.convert("L")
# my_convert.show()
# -----------------------------------------------------------------------

# try:
#     print(10/0)
#     print("hello")# print when no error وتقدر تستخدمها بدل else
#     print(int("hello"))
# except ZeroDivisionError:# تقدر تحدد العملية علي حسب نوع الخطا
#     print("hello from nun")  
# except NameError:
#     print("this name error")
# except ValueError:
#     print("ValueError")
# except:#تقدر تحط except لو مكنتش عارف نوع الخطا بس لازم ميكنوش بعديها except تانية
#     print("error habend")              
# else:#if no error
#     print("this is integer")
# finally:# بينفذ سواء كان في خطا او لا
#     print("print from finally what ever habens")
# # ملحوظة يقوم بالتعامل مع اول خطا واذا تم حاه يتعامل مع الثان فقط وهاكذا حتي تنتهي جميع الاخطاء
# -----------------------------------------------------------------------

# import re
# # my_string=re.search(r"[A-z]+\W[A-z]+\.[A-z]+", "Ahmed@gmail.com")
# # try:
# #     print(my_string.group())
# # except:
# #     print("there is a problem")
# # finally:
# #     print("finished")
# my_string=re.split(r"\s+|,\s+|,+", "ahmed Magdy, atalla,abdalazez")
# #my_string=re.split(r"\s+|,\s+|,+", "ahmed Magdy, atalla,abdalazez", 2)
# print(my_string)
# ##this a video from 102 i dont write here such as a group and groups
# my_string=re.findall(r"\w+|\s+", "ahmed Magdy, atalla,abdalazez" \
# "ahmed was here",re.MULTILINE or re.I)
# print("".join(my_string))
# my_string=re.sub(r"\W+|\W\s+"," " ,"ahmed Magdy, atalla,abdalazez")
# print(my_string)
# -----------------------------------------------------------------------

# ##video 118
# # import sqlite3
# # db=sqlite3.connect("app.db")
# # db.execute(
# #     "create table if not exists skills (name text, progress integer, user_ip integer)")
# # db.close
###=============
# ##video 119
# import sqlite3
# db=sqlite3.connect("app.db")
# cr=db.cursor()
# cr.execute("" \
# "create table if not exists skills (name text, progress integer, user_id integer)")
# cr.execute("create table if not exists users (user_id integer, name text)")
# # cr.execute("insert into users(user_id, name) values(1, 'Ahmed')")
# users_names=["Ahmed", "Mohamed", "Atalla"]
# for x, z in enumerate(users_names):
#     cr.execute(f"insert into users(user_id, name) values({x+1},'{z}')")
# db.commit()
#db.close()
###video 120
# import sqlite3
# name_list=["Ahmed", "Mohamed", "Magdy", "Abd Allah"]
###===================
###120
# import sqlite3
# name_list=["Ahmed", "Mohamed", "Magdy", "Abd Allah"]
# def reed():
#     try:
#         db=sqlite3.connect("app.db")
#         cr=db.cursor()
#         cr.execute(rf"create table if not exists users(name text, user_id integer)")
#         for x, z in enumerate(name_list):
#             cr.execute(rf"insert into users(user_id, name) values ({x+1}, '{z}')")
#         db.commit()
#     except:
#         print("error")
#     finally:
#         db.commit()
# reed()
###=====================
###video 121
# import sqlite3
# def reed():
#  try:
#         db=sqlite3.connect("app.db")
#         cr=db.cursor()
#         cr.execute(r"select * from users")
#         data=cr.fetchall()
#         for x, z in data:
#             print(f"your name is [{x}]:\nyour id is [{z}]")
#         db.close()
#  except:
#      print("Error")
# reed()
# -----------------------------------------------------------------------

###video 129
# import timeit
# print(timeit.timeit(""""Ahmed"*50"""))
# print(timeit.timeit("""random.randint(10, 50)""", setup="import random"))
# print(timeit.repeat(""""ahmed"*50""", repeat=5))
# -----------------------------------------------------------------------

###131
# assert type("ahmed")==str, "should be string"
# import unittest
# class MyTestCase(unittest.TestCase):
#     def test_1_class(self):
#         self.assertTrue(10>1, "should be true")
#     def test_2_class(self):
#         self.assertEqual(50+70, 120, "Should be 120")
#     def test_3_class(self):
#         self.assertGreater(5, 4, "ok")
# unittest.main()
# -----------------------------------------------------------------------

# import numpy as np
# my_list=[1, 2, 3, 4, 5]
# my_array=np.array(my_list)#, my_array=np.array(1, 2, 3, 4, 5) can be this to
# print(type(my_list))
# print(type(my_array))
# print(my_list[0])
# print(my_array[0])
# print(my_array.ndim)
# -----------------------------------------------------------------------