# по книге Майкла "Программируем на Python"
#компьютер выбирает случайное слово(из доступных в константе WORDS), пользователь их отгадывает
import random

WORDS =("питон","простоя", "сложная", "ответ", "подстаканник", "глупость")


word = random.choice(WORDS)#случайным образом выберем одно слово
correct = word #правильная версия слова
jumble = ""#переменная для пустой анаграммы

while word:#пока word содяржит хотя-бы одну букву:
	position = random.randrange(len(word))#изъять из слова случайную букву
	jumble += word[position]#присоеденяем букву к анаграмме
	word = word[:position]+word[(position+1):]
	#|создан оновленный вариант строки word =, в которой не будет сожержаться буква с индексом position. С помощью срезов компьютер извлекает
	#из word две подстроки. Первый срез - все буквы с с начала слова от word[position] до конца слова. Конкатенацию мы делаем значением 
	#переменной word, которая равна самой себе за вычетом одной буквы word[position] 
#приветствуем игрока
print(

"""
			Welcome to anagrams game!
		Try to know what word i've hide for u.
		(if you wanna exit, press Enter)
"""
	)
print("It's your anagram: ", jumble)

guess = input("\n Try to know hidden word: ")
attempts = 0

while guess != correct and guess !="":
	print("You aren't right")
	guess = input("Try to know hidden word: ")
	attempts += 1
	if attempts > 4:
		print( "Right word: ", correct)
		
if guess == correct:
	print("You are right!\n")
	print("thank you for game")
if attempts:
	print("\nBut you hasn't any scores:(")
else:
	print("\nWell done ")