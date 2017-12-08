#Harsh Bhardwaj
#A Coffee File Management Program

#Import the module that we created
import BhardwajH_coffee_records
import BhardwajH_coffee_inventory
import BhardwajH_coffee_search
import BhardwajH_coffee_modify
import BhardwajH_coffee_delete

#Global variable for adding your choice
add_choice = 1
#Global Variable for showing inventory
show_inventory = 2
#Global Variable for searching the inventory
search_inventory = 3
#Global Variable to modify record
modify_coffee = 4
#Global Variable to delete a record
delete_coffee = 5
#Global variable to quit
no_choice = 9

def main():
        choice = 0
        while choice != no_choice:
                user_menu()
                choice = int(input('Enter your choice: '))
                if choice == add_choice:
                        VardhanH_coffee_records.add_coffee()
                elif choice == show_inventory:
                        VardhanH_coffee_inventory.show_coffee()
                elif choice == search_inventory:
                        VardhanH_coffee_search.search_coffee()
                elif choice == modify_coffee:
                        VardhanH_coffee_modify.modify_coffee()
                elif choice == delete_coffee:
                        VardhanH_coffee_delete.delete_coffee()
                elif choice == no_choice:
                        print('Exiting the Menu...')
                else:
                        print('Error: Invalid Selection.')
	
def user_menu():
	print('eCon COFFEE MANAGEMENT MENU')
	print('1) Add more Coffee Choices to List')
	print('2) Show inventory')
	print('3) Search Coffee')
	print('4) Modify Coffee')
	print('5) Delete Coffee')
	print('9) Quit')
	
main()
