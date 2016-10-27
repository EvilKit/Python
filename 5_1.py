import random

WORDS = ["OVER", "CLAM","SNOW","PYTHON","EGG","CAKE","CORE"]
while WORDS != []:
    word = random.randrange(len(WORDS))
    print(WORDS[word])
    WORDS.remove(WORDS[word])
