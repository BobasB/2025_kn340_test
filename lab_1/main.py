from random import choice
from typing import List

WORDS = ["apple", "banana", "Python", "orange"]

def choose_secret_word(words: List[str]) -> str:
    return choice(words)

def enter_letter_from_user()-> str:
    letter = input("Введіть одну літеру: ")
    return letter.lower()

def check_letter_in_word(letter: str, word: str) -> str:
    return 
