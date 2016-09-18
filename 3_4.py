#Отгадай число (по учебнику М.Доусона)


print("Добро пожаловать в игру угадай число!")
print("Вы должны загадать число от 1 до 100, а компьютер его отгадает")
print("Начинаем:")

#начальные значения
number = int(input("Ваше число: "))
tries = 1
pc_guess = 50

#цикл отгадывания
while number > 100:
	number = int(input("Ваше число: "))
while pc_guess != number:
	
	if pc_guess > number:
		pc_guess=25
		tries += 1	
		if pc_guess > number:
			pc_guess=13
			tries += 1	
		if pc_guess > number:
			pc_guess-=1
			tries += 1	

	else:
		pc_guess += 1
	tries += 1	
if pc_guess == number:
	print("КОмпьютер это сделал!")
	print("Ваше число: ", pc_guess)
	print("На это он потратил всего ",tries," попыток\n")