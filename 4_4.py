import random

WORDS =("питон","простоя", "сложная", "ответ", "подстаканник", "глупость")
word = random.choice(WORDS)#случайным образом выберем одно слово

print("Word length: ", len(word))

tries = 5

while tries != 0:
	u_input = input("Enter your letter: ")
	if u_input in word:
		print("Да")
	else:
		print("Нет")
	tries -= 1

u_input = input("Enter your word: ")
if u_input ==word:
	print("You have won")
else:
	print("Game over")