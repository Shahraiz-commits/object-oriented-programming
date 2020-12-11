class Human:
    def __init__(self, a, h, n):
        self.__age = a
        self.__height = h
        self.__name = n
    def TellName(self):
        return self.__name
    def TellAge(self):
        return self.__age
    def TellHeight(self):
        return self.__height
    def TellAll(self):
        all = self.__name + " " + self.__age + " " + self.__height
        return all

class Teacher(Human):
    def __init__(self, a, h, n, qua, sub, exp):
        Human.__init__(self, a, h, n)
        self.__qualificaiton = qua
        self.__subject = sub
        self.__experience = exp

    def GetQualification(self):
        return self.__qualificaiton

    def GetSubject(self):
        return self.__subject

    def GetExperience(self):
        return self.__experience

    def GetAll(self):
        all = super().TellAll()
        all = all + self.__subject + " " + self.__experience + " " + self.__qualificaiton
        return all 

#test for Human class
Human1 = Human("18 years", "6ft", "Alex")
Human2 = Human("21 years", "5ft", "Dana")
print(Human1.TellAll())
print(Human2.TellAll())

#test for subclass Teacher
Human3 = Teacher("35 years", "7ft", "Daniel", "masters", "computer science", "10 years")
print(Human3.GetAll())
