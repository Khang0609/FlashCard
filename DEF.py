import codecs
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

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