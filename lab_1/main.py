from random import choice
from typing import List, Set

WORDS = ["apple", "banana", "python", "orange"]

def choose_secret_word(words: List[str]) -> str:
    return choice(words)

def enter_letter_from_user()-> str:
    letter = str(input("Введіть одну літеру: "))
    return letter.lower()

def check_letters_in_word(letters: Set[str], word: str) -> str:
    if word == "":
        raise ValueError("Word cannot be empty")
    return "".join([l if l in letters else "*" for l in word])

def check_if_word_guessed(letters: Set[str], word: str) -> bool:
    return all(l in letters for l in word)

def main():
    secret_word = choose_secret_word(WORDS)
    #print(f"Загадане слово: {secret_word}")
    entered_user_letters = set()
    for _ in range(len(secret_word) + 3):
        entered_user_letters.add(enter_letter_from_user())
        result = check_letters_in_word(entered_user_letters, secret_word)
        print(f"Введені значення: {entered_user_letters} \nРезультат: {result}")
        if check_if_word_guessed(entered_user_letters, secret_word):
            print("Ви вгадали слово!")
            break
    if not check_if_word_guessed(entered_user_letters, secret_word):
        print("Ви програли!")
    print(f"Гра завершена. Загадане слово було: {secret_word}")

if __name__ == "__main__":
    main()
