class User(object):
	access_level=1
	name=''
	def __init__ (self, name):
		self.name =  name
	def can_access(self, level): #levels which the user has access to
		return self.access_level >= level

class Employee(User):
	access_level = 2
	def can_access(self, level):
		return self.access_level >= level or level == 3
		#Employee can access level less than or eqaul to three

class Manager(Employee):
	access_level =3
	def can_access(self, level):
		return (self.access_level >= level or level in [2,6])
		#Manager can access levels 1,2 and 6

daisy = User("Daisy")
andela = Employee("Andela")
john = Manager("Kamanu")
users = [daisy,andela,john]

for level in range(1,7):
	for u in users:
		print u.name + " can access. level " + str(level) + ' ' + str(u.can_access(level))
	print "\n"
