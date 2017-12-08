#Harsh Bhardwaj
#Primary Election Ballot Program

class Voter:

	def __init__(self, firstname, lastname, idnumber):
		self.__firstname = firstname
		self.__lastname = lastname
		self.__idnumber = idnumber

	#Methods are mutators for the class's data attributes
	def set_firstname(self, firstname):
		self.__firstname = firstname

	def set_lastname(self, lastname):
		self.__lastname = lastname

	def set_idnumber(self, idnumber):
		self.__idnumber = idnumber

	#Methods are accessors for the class's data attributes
	def get_firstname(self):
		return self.__firstname

	def get_lastname(self):
		return self.__lastname

	def get_idnumber(self):
		return self.__idnumber

	propa = input("Are you in favor of or opposed to Proposition A? Y or N")
	if propa == 'Y' or 'yes' or 'y':
		print(True)
	elif propa == 'N' or 'no' or 'n':
		print(False)
	else:
		print('Not a valid answer.')
