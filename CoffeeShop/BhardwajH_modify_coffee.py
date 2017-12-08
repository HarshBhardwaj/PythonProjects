#Harsh Vardhan
#This module will modify the record in the file

import os

def modify_coffee():
	found = False

	search = input('Enter a description to search for: ')
	new_qty = int(input('Enter the new quantity: '))

	coffee_file = open('coffee.txt', 'r')

	temp_file = open('temp.txt', 'r')

	descr = coffee_file.readline()

	while descr != '':
		quantity = float(coffee_file.readline())

		descr = descr.rstrip('\n')

		if descr == search:
			temp_file.write(descr + '\n')
			temp_file.write(str(new_qty) + '\n')

			found = True
		else:
			temp_file.write(descr + '\n')
			temp_file.write(str(quantity) + '\n')
		descr = coffee_file.readline()

	coffee_file.close()
	temp_file.close()

	os.remove('coffee.txt')

	os.rename('temp.txt', 'coffee.txt')

	if found:
		print('The file has been updated.')
	else:
		print('That item was not found in the file.')