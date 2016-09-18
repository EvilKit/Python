import random

counter = 0


while counter != 100:
	coin = random.randint(1,2)
	if coin == 1:
		print("Орел")
	elif coin == 2:
		print("Решка")
	counter+=1