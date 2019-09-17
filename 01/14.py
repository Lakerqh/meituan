class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def print_score(self):
        print(self.__name,self.__score)


bart = Student('jack',100)
bart.print_score()
print(bart._Student__name)
