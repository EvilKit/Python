
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
EMPTY = ""
TIE = "Ничья"
NUM_SQUARES = 9

#Функции
def display_instruct():
    print("""Это инструкция к игре крестики-нолики.
            | 0 | 1 | 2 |
            _____________
            | 3 | 4 | 5 |
            _____________
            | 6 | 7 | 8 |

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

def pieses():#определяет кому достанется первый ход
    go_first = ask_yes_no("Хочешь ходить первым?")
    if go_first == "y":
         print("Ладно, даю тебе фору: играй крестиками.")
         human = X
         computer = O
    else:
        print("Твоя удаль тебя погубит. Буду начинать я.")
        human = O
        computer = X
def new_board():#Создает новую доску
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):#Отображает игровую доску на экране
    print("\n\t", board[0], "|", board[1], "|" , board[2])
    print("---------")
    print("\n\t", board[3], "|", board[4], "|" , board[5])
    print("---------")
    print("\n\t", board[6], "|", board[7], "|" , board[8],"\n")
    print("---------")

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
        move = ask_number("Твой ход. Выбери одно из полей (0 - 8)", O, NUM_SQUARES)
        if move not in legal:
            print("\nСмешной человек! Это поле уже занято. Выбери другое.\n")
        print("Ладно...")
        return move
def computer_move(board, computer, human):#Ход ИИ
    board = board[:]
    BEST_MOVES = (4, 0 , 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу поле номер", end = " ")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
        #Дальше я устал. Спокойной ночи.
