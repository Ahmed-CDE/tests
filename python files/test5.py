class test:
    num_of_user=0
    user_list=[]
    def __init__(self, name="", age=0 , country=""):
        self.name=name
        self.age=age
        self.country=country
        self.user_list.append(self)
    def say_hello(self):
            return f"hello {self.name}"
    def age_user(self):
            return f"your age is {self.age}"
    def country_1(self):
            if self.country:
             return f"{self.country} is a nice city"
            else:
                  return f"you dont enter your country name".title()
    def all(self):
            return f"{self.say_hello()}\n{self.age_user()}\n{self.country_1()}"
exit_loop=""
while exit_loop!="yes" and exit_loop!="y":
       name=input("pleas input your name: ".title()).strip()
       age=input("pleas input your age: ").title().strip()
       while type(age)!=int:
        try:
              age=int(age)
        except:
              age=input(f"you input [{age}] pleas input integer: ").title()
       country=input("pleas input your country name: ".title()).strip()
       name=test(name, age, country)
       exit_loop=input("do you want exit: ".title()).lower().strip()
def print_user(list):
       print({"data".center(20, "#")})
       for x in list:
              print(f"{x.all()}\n{"="*50}")
print_user(test.user_list)