#Игра по мотивам Висельницы.
#Часть кода принадлежит М.Доусону.
#Игра была написана в оброзовательных целях.

import random

#константы:
HANGMAN = (
"""
---------
|       |
|
|
|
|
|
------------
""",
"""
---------
|       |
|       0
|
|
|
|
------------
""",
"""
---------
|       |
|       0
|       |
|
|
|
------------
""",
"""
---------
|       |
|       0
|     \-|-/
|
|
|
------------
""",
"""
---------
|       |
|       0
|     \-|-/
|       |
|
|
------------
""",
"""
---------
|       |
|       0
|     \-|-/
|       |
|
|
------------
""",
"""
---------
|       |
|       0
|     \-|-/
|       |
|      |
|
------------
""",
"""
---------
|       |
|       0
|     \-|-/
|       |
|      | |
|
------------
"""
)
MAX_WRONG = len(HANGMAN)-1
WORDS = ["OVER", "CLAM","SNOW","PYTHON","EGG","CAKE","CORE"]


print("Добро пожаловать в игру 'Висельница'. Удачи вам!")
choise = None
while choise != "0":
	word = random.choice(WORDS)
	so_far = "-"*len(word) #набор дефисов, по одному на каждую букву
	wrong = 0#Ошибки, допушеные игрокам(кол-во)
	used=[]#буквы, которые игрок уже предлагал
	print(
	"""
	\tОпции:
	\t0 - выход
	\t1 - начать игру
	\t2 - добавить слово
	\t3 - удалить слово
	""")
	choise = input("Ваш выбор: ")
	if choise == "0":
		print("До встречи!")
	elif choise == "2":
		term = input("Какое слово вы хотели бы добавить? \n")
		if term not in WORDS:
			WORDS.append(term)
			print("\nСлово", term, "было добавлено")
		else:
			print("\nЭто слово уже есть в словаре.")
	elif choise == "3":
		term = input("Какое слово вы хотите удалить? \n")
		if term in WORDS:
			del WORDS[term]
			print("\nСлово", term, "было удалено")
		else:
			print("\nНичего нет")
	elif choise == "1":
		while wrong != MAX_WRONG and so_far != word:
			print(HANGMAN[wrong])
			print("\nВы уже предлагали:\n", used)
			print("\nСлово сейчас выглядит так:\n", so_far)
			guess = input("Введите букву: ")
			guess = guess.upper()#переводим у верхнему регистру
			#проверка: не вводил ли игрок эту букву ранее
			while guess in used:
				print("Вы уже предлагали эту букву: ",guess, "Попробуйте ввести другую.")
				guess = input("\nВведите букву: ")
				guess = guess.upper()
				#добавляем букву к used
			used.append(guess)

			#проверка наличия буквы в слове
			if guess in word:
				print("Да! Буква", guess, "действительно находится в слове!")
				#новая строка so_far с отгаданой буквой в слове:
				new=""
				for i in range(len(word)):
					if guess == word[i]:
						new += guess
					else:
						new += so_far[i]
				so_far = new
			else:
				print("Буквы", guess, "нет в слове!")
				wrong += 1

	#завершение игры
		if wrong == MAX_WRONG:
			print(HANGMAN[wrong])
			print("\nВас повесили!")
		else:
			print("\nВы отгадали!")
		print("\nБыло загадано слово", word)
		input("\nНажмите Enter, чтобы выйти.")
