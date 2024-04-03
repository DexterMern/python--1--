class Question:
    def __init__(self, q: list, a: list):
        self.q = q
        self.a = a


class ExamPaper:
    def __init__(self):
        self.question = Question('what is your name?', ['reza', 'ali', 'mohammad'])

    def __str__(self):
        return f'{self.question.q}\n{self.question.a}'


class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f'{self.name}: {self.number}'


class University:
    def __init__(self, students):
        self.students = students


st = [Student('naser', '12'), Student('mahsa', '98')]
university = University(st)
for s in university.students:
    print(s)
print(40*'_')
e = ExamPaper()
print(e)
