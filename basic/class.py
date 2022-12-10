

class Dog():
    """构造函数"""
    def __init__(self, name, age):
        #super(ClassName, self).__init__()
        self.name = name
        self.age = age
        
    def sit(self):
        print(self.name.title() + " is sitting now.")

    def run(self):
        print(self.name.title() + " is running now.")

reddog = Dog("reddog",3)
reddog.sit()

class NewDog(Dog):    #父类是Dog
    def __init__(self,name,age):
        super().__init__(name,age)
        self.type = 'erha'

    def dogtype(self):
        print(self.name.title() + " is " +self.type.title() + ".")

greendog = NewDog("jhone",2)
greendog.dogtype()