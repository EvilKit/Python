# Переводчик с гикского на русский

# Демонстрирует использование словарей

geek = {"404": "Не знать. не владеть информацией. От сообщения об ошибке 404 'Стра­ница не найдена'.",
"Googling": "'Гугление·. nоиск в Сети сведений о ком-либо.","Keyboard Pl aque" : "Мусор. который скапливается в клавиатуре компьютера.",

"L ink Rot" : "Процесс устаревания гиперссылок на веб-страницах . ",

"Percussive Maintenance" : "О ситуации. когда кто-либо бьет по корпусу не-исправного электронного прибора в надежде восстановить его работу.",

"Uninstalled" : "Об увольнении кого-либо. Особенно популярно на рубеже1990-2000-х годов "}
choise = None
while choise != "0":
	print(
	"""
	Geek translator
	\tOptions:
	\t0 - exit
	\t1 - search term
	\t2 - add term
	\t3 - edit term
	\t4 - delete term
	""")
	choise = input("Your choise: ")
	if choise == "0":
		print("Goodbye")
	
	elif choise == "1":
		term = input("Which term do you wanna translate? \n")
		if term in geek:
			definition = geek[term]
			print("\n", term, "means", definition)
		else:
			print("\nNo such term :( :", term)

	elif choise == "2":
		term = input("Which term do you wanna add? \n")
		if term not in geek:
			definition = input("\nEnter your definition: ")
			geek[term] = definition
			print("\nTerm", term, "has been added to vocabulary")
		else:
			print("\nThis term has already been added! Try to edit his definition.")

	elif choise == "3":
		term = input("Which term do you wanna edit? \n")
		if term in geek:
			definition = input("Enter your definition")
			geek[term] = definition
			print("\nTerm", term, "has been edited")
		else:
			print("\nNo such term :(")

	elif choise == "4":
		term = input("Which term do you wanna delete? \n")
		if term in geek:
			del geek[term]
			print("\nTerm", term, "has been deleted")
		else:
			print("\nNo such term :(")