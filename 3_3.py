#Отгадай число (по учебнику М.Доусона)
import random

print("Добро пожаловать в игру угадай число!")
print("Вы должны отгадать одно число от 1 до 100 за 10 попыток")
print("Начинаем:")

#начальные значения
number = random.randint(1,100)
guess = int(input("Ваше предположение: "))
tries = 10

#цикл отгадывания
while guess != number:
	if guess > number:
		print("меньше...")
	else:
		print("больше...")
	guess = int(input("Ваше предположение: "))
	tries -= 1
	if tries <= 0:
		print("Вы проиграли!")
		break		
if guess == number:
	print("Вы это сделали!")
	print("На это вы потратили всего ",10-tries," попыток\n")