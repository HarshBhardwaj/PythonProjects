#Harsh Vardhan
#Show the inventory of the coffee

def show_coffee():
	#Open the coffee.txt file.
	coffee_file = open('coffee.txt', 'r')
	
	#Read the first record's description field.
	descr = coffee_file.readline()
	
	#Read the rest of the file.
	while descr != '':
		#Read the quantity field.
		quantity = float(coffee_file.readline())
		
		#Strip the \n from the description.
		descr = descr.rstrip('\n')
		
		#Display the record.
		print('Description:', descr)
		print('Quantity:', quantity)
		
		#Read the next description.
		descr = coffee_file.readline()
		
	#Close the file.
	coffee_file.close()