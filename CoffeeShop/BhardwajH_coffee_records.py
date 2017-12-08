#Harsh Vardhan's coffee record

def add_coffee():
	#create a variable to control the loop.
	another = 'y'
	
	#open the coffee.txt file in append mode.
	coffee_file = open('coffee.txt', 'a')
	
	#Add records to the file.
	while another == 'y' or another == 'Y':
		#Get the coffee record data.
		print('Enter the following coffee data: ')
		descr = input('Description: ')
		quantity = int(input('Quantity (in pounds): '))
		
		#Append the data to the file.
		coffee_file.write(descr + '\n')
		coffee_file.write(str(quantity) + '\n')
		
		#Determine whether the user wants to add another record to the file.
		print('Do you want to add another record? ')
		another = input('Y = yes, anything else = no: ')
		
	#Close the file.
	coffee_file.close()
	print('Data append to coffee.txt')