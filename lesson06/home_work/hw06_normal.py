# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

import random

class Person(object):
	"""docstring for Person"""
	def __init__(self):
		super(Person, self).__init__()
		
		up_letters = [chr(x) for x in range(ord('A'), ord('Z'))]
		low_letters = [chr(x) for x in range(ord('a'), ord('z'))]
		self.name = up_letters[random.randint(0, len(up_letters)-1)] + \
					''.join([low_letters[random.randint(x, len(low_letters)-1)] for x in range(0,random.randint(5,10))]) + ' ' + \
					up_letters[random.randint(0, len(up_letters)-1)] + '.' + \
					up_letters[random.randint(0, len(up_letters)-1)] + '.'

class Pupil(Person):
	"""docstring for Pupil"""
	def __init__(self, schoolclass):
		super(Pupil, self).__init__()
		schoolclass.pupils.append(self)
		self.schoolclass = schoolclass
		self.parents = [Parent(self) for x in range(0,2)]
		
class Parent(Person):
	"""docstring for Parent"""
	def __init__(self, child):
		super(Parent, self).__init__()
		self.child = child

		
class Teacher(Person):
	"""docstring for Teacher"""
	def __init__(self, subject):
		super(Teacher, self).__init__()
		self.subject = subject

		
class SchoolSubject(object):
	"""docstring for Subject"""
	def __init__(self):
		super(SchoolSubject, self).__init__()
		up_letters = [chr(x) for x in range(ord('A'), ord('Z'))]
		low_letters = [chr(x) for x in range(ord('a'), ord('z'))]
		self.title = up_letters[random.randint(0, len(up_letters)-1)] + ''.join([low_letters[random.randint(x, len(low_letters)-1)] for x in range(0,random.randint(5,10))])


class SchoolClass(object):
	"""docstring for SchoolClass"""
	def __init__(self, teachers):
		super(SchoolClass, self).__init__()
		self.teachers = teachers
		self.title = str(random.randint(1, 10)) + chr(random.randint(ord('A'),ord('Z')))
		self.pupils = []
		
class School(object):
	"""docstring for School"""
	def __init__(self, title):
		super(School, self).__init__()
		self._title = title
		self.subjects = [SchoolSubject() for x in range(0, 19)]
		self.teachers = [Teacher(self.subjects[x]) for x in range(0, 19)]
		self.classes = [SchoolClass(random.sample(self.teachers, 5)) for x in range(1, 20)]
		self.pupils = [Pupil(self.classes[random.randint(0, len(self.classes)-1)]) for x in range(1, 100)]

	@property
	def title(self):
		return self._title.capitalize()
	
	
	
	

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

school = School('School №3')
print(school.title)

print('Clases: ', ', '.join([x.title for x in school.classes]))

while True:
	print(f"Input number class from 1 to {len(school.classes)}: ")
	need_class = int(input()) - 1
	if need_class < len(school.classes):
		break

need_class = school.classes[need_class]
print(f"Pupils of class {need_class.title}: ", ', '.join([x.name for x in need_class.pupils]))

while True:
	print(f"Input number pupil from 1 to {len(need_class.pupils)}: ")
	need_pupil = int(input()) - 1
	if need_pupil < len(need_class.pupils):
		break

need_pupil = need_class.pupils[need_pupil]
print(f"Subjects of pupil {need_pupil.name} from class {need_class.title}: ", ', '.join(x.subject.title for x in need_pupil.schoolclass.teachers))

print(f"Parents of pupil {need_pupil.name} from class {need_class.title}: ", ', '.join(x.name for x in need_pupil.parents))

print(f"Teachers of class {need_class.title}: ", ', '.join(x.name for x in need_class.teachers))

