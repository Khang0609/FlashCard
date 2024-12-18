from DEF import *
from path import *

def main():
    dont_remember = []
    word_list = getVocabList(HKI)
    firstAsk(word_list, dont_remember)
    reviewAll(dont_remember)

main()