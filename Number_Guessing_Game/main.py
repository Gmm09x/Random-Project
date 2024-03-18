#!/usr/bin/python3



import random
import time
import os




def Random_Number():
	Random_numbers = random.randint(0, 11)

	return Random_numbers


def main(MAIN_NUMBER):

	main_number = MAIN_NUMBER

	Conut = 0
	while True:
		User_Guess_Number = input("\n[+]Guess The Number: ")

		if User_Guess_Number:

			if User_Guess_Number.isnumeric():
				Conut += 1
				User_Guess_Number = int(User_Guess_Number)

				if User_Guess_Number == main_number:
						print(f"[+](: You Find The Number: {main_number}")
						print(f"\n[+]Number Of Try: {Conut}")
						break


				elif User_Guess_Number > main_number:
						print("[*]}: Your Number is upper")
				else:
					print("[*][:Your Number is Lower")

			else:
				print("Only Numbers Plaese...")
				time.sleep(1)
				os.system("clear")

		else:
			print("Plaese Guess The Number...")
			time.sleep(1)
			os.system("clear")




if __name__ == '__main__':
	a = Random_Number()
	# print(a)
	main(a)