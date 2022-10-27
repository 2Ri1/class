class Student:
	def __init__(self, name, surname, gender):
		self.name = name
		self.surname = surname
		self.gender = gender
		self.finished_courses = []
		self.courses_in_progress = []
		self.grades = {}
		self.courses_attached = []
	def rate_l(self, lecturer, course, grade):  
		if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
			if course in lecturer.grades:
				lecturer.grades[course] += [grade]
			else:
				lecturer.grades[course] = [grade]
		else:
			return 'Ошибка'   	
	def _middle_grade(self):
		self.mid_grade = sum(sum(self.grades.values(),[]))/len(sum(self.grades.values(),[]))
		return self.mid_grade
	def __str__(self):
		res = f'Имя: = {self.name} \nФамилия: = {self.surname}\nСредняя оценка за домашние задания: = {self._middle_grade()}\nКурсы в процессе изучения: = {",".join(self.courses_in_progress)}\nЗавершенные курсы: = {",".join(self.finished_courses)}'
		return res		
	def __lt__(self, other):
		if not isinstance(other, Student):
			print('Not a Student!')
			return
		return self._middle_grade() < other._middle_grade()	
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
	def __init__(self, name, surname, gender):
		self.gender = gender
		self.grades = {}
		self.courses_attached = []
		self.courses_in_progress = []
	def _middle_grade(self):
		self.mid_grade = sum(sum(self.grades.values(),[]))/len(sum(self.grades.values(),[]))
		return self.mid_grade
	def __str__(self):
		res = f'Имя: = {self.name} \nФамилия: = {self.surname} \nСредняя оценка за лекции: = {self._middle_grade()}'
		return res	
	def __lt__(self, other):
		if not isinstance(other, Lecturer):
			print('Not a Lecturer!')
			return
		return self._middle_grade() < other._middle_grade()	
class Reviewer(Mentor):
	def rate_hw(self, student, course, grade):
		if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
			if course in student.grades:
				student.grades[course] += [grade]
			else:
				student.grades[course] = [grade]
		else:
			return 'Ошибка'
	def __str__(self):
		res = f'Имя: = {self.name} \nФамилия: = {self.surname}'
		return res

Ema = Student('Ema', 'Wilson', 'female')
Ema.courses_in_progress += ['basics']
Ema.courses_attached += ['basics']

Amber = Student('Amber', 'Davies', 'female')
Amber.courses_in_progress += ['Python']
Amber.courses_attached += ['Python']
Amber.courses_attached += ['git']
Amber.finished_courses = ['basics']

Bob = Reviewer('Bob', 'Brown')
Bob.courses_attached += ['basics']

William = Reviewer('William', '	Moore')
William.courses_attached += ['Python']

Ethan = Lecturer('Ethan', '	Ellington', 'male')
Ethan.courses_in_progress += ['git']
Ethan.courses_attached += ['basics']
Ethan.courses_in_progress += ['basics']

Oscar = Lecturer('Oscar', '	Lewis', 'male')
Oscar.courses_in_progress += ['git']
 
Bob.rate_hw(Ema, 'basics', 10)
Bob.rate_hw(Ema, 'basics', 10)
Bob.rate_hw(Ema, 'basics', 9)

William.rate_hw(Amber, 'Python', 5)
William.rate_hw(Amber, 'Python', 8)
William.rate_hw(Amber, 'Python', 6)

print(Ema.grades)
print(Amber.grades)

Ema.rate_l(Ethan, 'basics', 9)
Ema.rate_l(Ethan, 'basics', 8)
Ema.rate_l(Ethan, 'basics', 10)

Amber.rate_l(Oscar, 'git', 10)
Amber.rate_l(Oscar, 'git', 8)
Amber.rate_l(Oscar, 'git', 10)

print(Ethan.grades)
print(Oscar.grades)

Ema.finished_courses = 'basics'
Ema.courses_in_progress = 'git', 'Python'

print(Amber)
print(Amber._middle_grade())
print(Ema._middle_grade())
print(Amber < Ema)

print(Ethan._middle_grade())
print(Oscar._middle_grade())
print(Ethan < Oscar)