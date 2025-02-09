#Still a work in progress, i will refactor later
import random

greeting = "Hellow dear player, i'll skip the worthless mumbojambo and get straight to the point.\nYou guess at least 3 numbers correctly and you'll win 1 million Satoshi ≈ 1 Bitcoin.There are only 3 rules, NO CHEATING!!!,UNLIMITTED TRIES and WIN!!!\n"
how_to_play = "It's simple, enter your 7 guess in the prompt below separated by comma\n"

print(greeting)
print("e.g: 60,38,9,0,33,2,21")
print("")

################################################
#first set
start = 0
end = 60
num_random = 7

#user guess
its_num_x = input("Enter your guess, separated by (,): ")
its_num = [int(x) for x in its_num_x.split(",")]
print(its_num)

#Random generated numbers
for _ in range(num_random):
				num_1 = random.randint(start, end)
				
				#check if user's guess is correct or not

				print(num_1, end=' ')
################################################