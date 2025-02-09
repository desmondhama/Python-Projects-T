#Still a work in progress, i will refactor later
import random

greeting = "Hellow dear player, i'll skip the worthless mumbojambo and get straight to the point.\nYou guess at least 3 numbers correctly and you'll win 1 million Satoshi ≈ 1 Bitcoin.There are only 3 rules, NO CHEATING!!!,UNLIMITTED TRIES and WIN!!!\n"
how_to_play = "It's simple, enter your 7 guess in the prompt below separated by comma\n"
des_email = "desmondhama@gmail.com"
print(greeting)
print("e.g: 60,38,9,0,33,2,21")
print("")

################################################

#user guess
its_num_x = input("Enter your guess, separated by (,): ")
its_num = list(map(int, its_num_x.split(",")))

#Random generated numbers
random_num = random.randint(range(60), 7)
				
	#find common nums
common_num = set(its_num) & set(random_num)
	
				#check if user's guess is correct or not
if len(common_num) <= 3:
				print(f"Congragulations you've won!!!\nSend me an email to {des_email} with a screenshot and BTC Wallet address")
else:
				print("ohh hard luck, feel free to try again though")
################################################