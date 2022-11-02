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
		res = f'Имя: = {self.name} \nФамилия: = {self.surname}\nСредняя оценка за домашние задания: = {round(self._middle_grade(),2)}\nКурсы в процессе изучения: = {",".join(self.courses_in_progress)}\nЗавершенные курсы: = {",".join(self.finished_courses)}'
		return res		
	def __lt__(self, other):
		if not isinstance(other, Student):
			print('Not a Student!')
			return
		return self._middle_grade() < other._middle_grade()	
	def mid_1(self):
		sum = 0
		count = 0
		for i in self.grades_1.values():
			for j in i:
				sum += j
				count += 1
			return sum/count
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
		res = f'Имя: = {self.name} \nФамилия: = {self.surname} \nСредняя оценка за лекции: = {round(self._middle_grade(),2)}'
		return res	
	def __lt__(self, other):
		if not isinstance(other, Lecturer):
			print('Not a Lecturer!')
			return
		return self._middle_grade() < other._middle_grade()	
	def _mid_1(self):
		sum = 0
		count = 0
		for i in self.grades.values():
			for j in i:
				sum += j
				count += 1
			return sum/count
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
Ema.courses_attached += ['Python']

Amber = Student('Amber', 'Davies', 'female')
Amber.courses_in_progress += ['Python']
Amber.courses_attached += ['basics']
Amber.courses_attached += ['git']
Amber.finished_courses += ['basics']
Amber.courses_attached += ['Python']

Bob = Reviewer('Bob', 'Brown')
Bob.courses_attached += ['basics']

William = Reviewer('William', '	Moore')
William.courses_attached += ['Python']
William.courses_attached += ['basics']

Ethan = Lecturer('Ethan', '	Ellington', 'male')
Ethan.courses_in_progress += ['git']
Ethan.courses_attached += ['basics']
Ethan.courses_in_progress += ['basics']

Oscar = Lecturer('Oscar', '	Lewis', 'male')
Oscar.courses_in_progress += ['basics']
 
Bob.rate_hw(Ema, 'basics', 10)
Bob.rate_hw(Ema, 'basics', 9)
Bob.rate_hw(Ema, 'basics', 9)

Bob.rate_hw(Ema, 'Python', 10)
Bob.rate_hw(Ema, 'Python', 6)
Bob.rate_hw(Ema, 'Python', 8)

William.rate_hw(Amber, 'basics', 5)
William.rate_hw(Amber, 'basics', 8)
William.rate_hw(Amber, 'basics', 6)

William.rate_hw(Amber, 'Python', 5)
William.rate_hw(Amber, 'Python', 8)
William.rate_hw(Amber, 'Python', 6)

print(f'\n Оценки Ema: {Ema.grades}')
print(f'\n Оценки Amber: {Amber.grades}')

Ema.rate_l(Ethan, 'basics', 9)
Ema.rate_l(Ethan, 'basics', 8)
Ema.rate_l(Ethan, 'basics', 10)

Amber.rate_l(Oscar, 'basics', 10)
Amber.rate_l(Oscar, 'basics', 8)
Amber.rate_l(Oscar, 'basics', 10)

print(f'\n Оценки Ethan: {Ethan.grades}')
print(f'\n Оценки Oscar: {Oscar.grades}')

Ema.finished_courses = 'basics'
Ema.courses_in_progress = 'git', 'Python'

print(f'\n Данные по студенту Amber: {Amber}')
print(f'\n Средняя оценка Amber: {round(Amber._middle_grade(),2)}')
print(f'\n Средняя оценка Ema: {round(Ema._middle_grade(),2)}')
print(f'\n У Amber средняя оценка ниже чем у Ema: {Amber < Ema}')

print(f'\n Средняя оценка Ethan: {round(Ethan._middle_grade(),2)}')
print(f'\n Средняя оценка Oscar: {round(Oscar._middle_grade(),2)}')
print(f'\n У Ethan средняя оценка ниже чем у Oscar: {Ethan < Oscar}')

d = []
g = []

def average_S(list, course):
	sum = 0
	count = 0
	for i in list:
		g.append(i.grades[course])
		for j in i.grades[course]:
			sum += j
			count += 1
		return round(sum/count, 2)

def average_L(list, course):
	sum = 0
	count = 0
	for i in list:
		d.append(i.grades[course])
		for j in i.grades[course]:
			sum += j
			count += 1
	return round(sum/count, 2)

print(f'\n Средняя оценка студентов: {average_S([Ema, Amber], "basics")}')
print(f'\n Средняя оценка лекторов: {average_L([Ethan, Oscar], "basics")}')
