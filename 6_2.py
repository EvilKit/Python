#Отгадай число (по учебнику М.Доусона)

def display_instruct():
	print("Добро пожаловать в игру угадай число!")
	print("Вы должны загадать число от 1 до 100, а компьютер его отгадает")
	print("Начинаем:")
	#начальные значения
def ask_number():
	number = int(input("Ваше число: "))

	while number > 100 or number < 0:
		number = int(input("Ваше число: "))
	return number
#цикл отгадывания
def guess(number):
	pc_guess = 50
	tries = 1
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
		print("Кoмпьютер это сделал!")
		print("Ваше число: ", pc_guess)
		print("На это он потратил всего ",tries," попыток\n")
def main():
	display_instruct()
	number = ask_number()
	guess(number)
main()
