#!/usr/bin/python3


import os
import time

MAIN_PROMPT = "Commands~$ "
MAIN_ITEMS_LIST = []


def clean():

	os.system("clear")



def Main_Time():

	time.sleep(1)



def Add_Items():
	clean()
	while True:
		User_Add_Items = input("Items Name: ")

		if User_Add_Items:
			MAIN_ITEMS_LIST.append(User_Add_Items)

			if User_Add_Items.lower() == "done":
				MAIN_ITEMS_LIST.pop(-1)
				break
		else:
			print("Please Enter a Name of Items You Want To Add In List")
			Main_Time()
			clean()



def Make_Items_Bill():
	clean()
	if MAIN_ITEMS_LIST == []:
		print("\n[-] ): Please Add Items First..")
		input("[-] Press Enter for Ok")
		clean()

	else:
		Count = 1
		for item in MAIN_ITEMS_LIST:
			print(f"{Count}: Item name: {item}")			
			Count += 1
		print(f"\n[+]Numbers Of Items in Your Lists: {Count-1}")
		print(f"[+]Totel Of Items Bill is $: {Count*4}")
		print("\nif Use Want Remove Item in List use:[remove_items] Command\n")



def Remove_Items_in_List():

	if MAIN_ITEMS_LIST == []:
		print("\n[-] ): Please Add Items First..")
		input("[-] Press Enter for Ok")
		clean()
	else:
		while True:
			Count = 0
			for item in MAIN_ITEMS_LIST:
				Count +=1
				print(f"{Count}: Item Name: {item}")

			Remove_Items_in_List_Number = input("Remove Item By is Name: ")
			
			if Remove_Items_in_List_Number:
				MAIN_ITEMS_LIST.remove(Remove_Items_in_List_Number)
				Make_Items_Bill()
				break
			else:
				print("Only Number Please...")
				Main_Time()
				clean()



def Help_Manu() -> str:

	help_main_page = """[How TO USE]
	[add_items]: Command for add Items
	[remove_items]: Command for Items in list
	[make_bill]: Command for make Items bill
	[help_menu]: Command for open help menu
	[exit]: Command for exit the progam"""
	return help_main_page




def main():
	clean()
	print("Walcome...")

	while True:
		User_Input = input(f"{MAIN_PROMPT}")

		if User_Input:
			
			if User_Input.lower() == "clear":
				clean()
			elif User_Input.lower() == "add_items":
				Add_Items()
			
			elif User_Input.lower() == "make_bill":
				Make_Items_Bill()

			elif User_Input.lower() == "exit":
				print("Thank You for Useing...")
				break

			elif User_Input.lower() == "remove_items":
				Remove_Items_in_List()

			elif User_Input.lower() == "help_menu":
				main = Help_Manu()
				print(main)
			
			else:
				print("Command Not Found ):, Please Try help_menu Command...")
				Main_Time()

		else:
			print("Please Enter Something...")
			Main_Time()

if __name__ == '__main__':
	main()


