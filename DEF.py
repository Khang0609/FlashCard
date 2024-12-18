import codecs
import random

# def remeberOrnot():
#     remember =int(input("Nhập 1 nếu bạn đã nhớ, 2 nếu bạn chưa nhớ nghĩa của từ: "))
#     if remember == 1:
#         return True
#     else:
#         return  False

# def ask(list_word):
#     print(f"Từ {list_word[0]} có nghĩa là gì?")
#     rememrber_check = remeberOrnot()
#     print(f"\nTừ {list_word[0]} có nghĩa là {list_word[1].upper()}\n")
#     return rememrber_check

# def first_ask(list_word, list_not):
#     for i in range(len(list_word)):
#         vocabulary = random.choice(list_word)
#         remember_check = ask(vocabulary)
#         if not(remember_check):
#             list_not.append(vocabulary)
#         list_word.remove(vocabulary)
#         print(len(list_word))
#     return len(list_word)

def getDefinition(file_lines, vocab_list):
    for line in file_lines:
        new_vocab_definition = line.rstrip("\n")
        vocab_list.append(new_vocab_definition.split(':'))

def getVocabList(file_path):
    vocab_list = [] # list of vocabulary
    with codecs.open(file_path, 'r') as f:
        file_lines = f.readlines()
    getDefinition(file_lines, vocab_list)
    return vocab_list

def dontRemember(word, dont_remember_list):
    dont_remember_list.append(word)

def ask(word, dont_remember_list):
    print(f"Từ {word[0].upper()} có nghĩa là gì?")
    if int(input("Nếu bạn không nhớ nghĩa từ này, nhấn phím 1\nNếu đã nhớ thì nhấn phím 2\n")) == 1:
        dontRemember(word, dont_remember_list)
    print(f"\nTừ này có nghĩa là {word[1].upper()}\n")

def firstAsk(words_list, dont_remember_list):
    for time in range(len(words_list)):
        word = random.choice(words_list)
        ask(word, dont_remember_list)

def reviewAll(dont_remember_list):
    while len(dont_remember_list) != 0:
        word = random.choice(dont_remember_list)
        ask(word, dont_remember_list)
        dont_remember_list.remove(word)