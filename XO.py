
'''
Немного о функциях:
display _iпstruct() - Выводит инструкцию для игрока

ask_yes_пo(questioп) - задает вопрос, ответом на который может быть «Да» или «Нет». Принимает текст вопроса, возвращает ''у" или "п"

ask_пumЬer(questioп, low,high() - Просит ввести число из указанного диапазона. Принимает текст
вопроса, нижнюю (low) и верхнюю (high) границы диапазона.
Возвращает целое число не меньше low и не больше high

pieces() - Определяет принадлежность первого хода человеку или ком-
пьютеру. Возвращает типы фишек соответственно компьютера и человека

пew_Ьoard() - Создает пустую игровую досху. Возвращает эту доску

display _Ьoard(board) - Отображает игровую доску на экране. Принимает эту доску

legal_moves(Ьoard) - Создает список доступных ходов. Принимает доску. Возвращает
список доступных ходов

wiпner(board) - Определяет победителя игры. Принимает доску. Возвращает тип
фишек победителя: "Ничья• или None

humaп_move(Ьoard, humaп) - Узнает, какой ход жеnает совершить игрок. Принимает доску
и тип фишек человека. Возвращает ход человека

computer _move(Ьoard, computer, human) Рассчитывает ход компьютерного противника. Принимает доску, тип фишек компьютера и тип фишек человека. Возвращает ход
компьютера

пext_tum(turп) - Осуществляет переход к следующему ходу. Принимает тип фи-
шек. Возвращает тип фишек

coпgrat_wiппer(the_winпer, computer, human) - Поздравляет победителя или констатирует ничью. Принимает
тип фишек победителя, тип фишек компьютера и тип фишек человека
'''
#--------Код--------

#Глобальные Константы
X = "X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9

#Функции
def display_instruct():
    print(
    """
Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех времен

Твой мозг и мой процессор сойдутся в схватке за доской игры "Крестики-нолики"

Чтобы сделать ход. введи число от О до 8. Числа однозначно соответствуют полям
доски - так. как показано ниже:
\t 0 | 1 | 2
\t---------
\t 3 | 4 | 5
\t---------
\t 6 | 7 | 8

Приготовься к бою. жалкий белковый человечишка. Вот-вот начнется решающее сра­жение.
    """)

def ask_yes_no(question):
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response

def ask_number(question,low,heigh):#просит ввести число из диапазона
    response = None
    while response not in range(low, heigh):
        response = int(input(question))
    return response

def ask_try_again(question):
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response

def pieces():#определяет кому достанется первый ход
    go_first = ask_yes_no("Хочешь ходить первым?(y,n): ")
    if go_first == "y":
         print("Ладно, даю тебе фору: играй крестиками.")
         human = X
         computer = O
    else:
        print("Твоя удаль тебя погубит. Буду начинать я.")
        human = O
        computer = X
    return computer, human

def new_board():#Создает новую доску
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):#Отображает игровую доску на экране
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "| ", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):#создает список доступных ходов
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):#Определяет победителя
    WAYS_TO_WIN = ( (0, 1, 2),
                    (3, 4, 5),
                    (6, 7, 8),
                    (0, 3, 6),
                    (1, 4, 7),
                    (2, 5, 8),
                    (0, 4, 8),
                    (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def human_move(board, human):#получает ход человека
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Tвoй ход. Выбери одно из полей (О - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nСмешной человек! Это поле уже занято. Выбери другое.\n")
        print("Ладно...")
        return move

def computer_move(board, computer, human):#Ход ИИ
    #Создадим рабочую копию доски, потому что функция будет менять некоторіе значения в списке
    board = board[:]
    #поля от лучшего к худшему
    BEST_MOVES = (4, 0 , 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу поле номер", end = " ")
    for move in legal_moves(board):
        board[move] = computer
        #если следуюшим ходом может победить компьютер, выберем этот ход
        if winner(board) == computer:
            print(move)
            return move
        #выполнив проверку, отменим внесенные изменения
        board[move] = EMPTY
        #Дальше я устал. Спокойной ночи.
        #Продолжим кодить:
    for move in legal_moves(board):
        board[move] = human
         #если следующим ходом может победить человек, блокируем этот ход
        if winner(board) == human:
             print(move)
             return move
         #выполнив проверку, отменим внесенные изменения
        board[move] = EMPTY
         #поскольку следующим ходом ни одна сторона не может победить
         #выборем лучшее из доступных полей
    for move in BEST_MOVES:
            if move in legal_moves(board):
                print(move)
                return move
def next_turn(turn):#Осуществляет переход хода
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):#Поздравляет победителя игры
    if the_winner != TIE:
        print("Три", the_winner, "в ряд!\n")
    else:
        print("Ничия!\n")
    if the_winner == computer:
        print("Как я и предпологал, люди не могут сравниться с железом, победа в очередной раз осталась за мной\n",\
        "Вот еще один довод в пользу того,что компьютеры превосходят людей решительно во всем!")
    elif the_winner == human:
        print("О нет, этого не может быть! Это.. это всего лишь случайность, в следующий раз ты не сможешь прехетрить меня, белковый!\n",\
        "Клянусь: я, компьютер, больше никогда этого не допущу!")
    elif the_winner == TIE:
        print("Тебе несказанно повезло, дружок: ты сумел свести игру вничью.\n",
        "Радуйся, тебе больше не суждено это повторить")

def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)
    wonna_play = ask_try_again("Хотите начать заново? (y, n): ")
    if wonna_play == 'y':
        main()
    else:
        print("Удачи")
    #Start prigramm
main()
input()
