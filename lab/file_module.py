# Цей модуль буде відповідати за генерацію слів які потрібно вгадати
import random

INITIAL_WORDS = ["apple", "banana", "cherry", "orange", "Python", "Developer", "function", "variable", "iteration", "condition"]

def get_n_random_words(n: int) -> list:
    if n > len(INITIAL_WORDS):
        raise ValueError("Кількість слів перевищує доступну.")
    return [w.lower() for w in random.sample(INITIAL_WORDS, n)]

def func_for_module_import():
    return "Ця функція призначена для тестування імпорту модуля."

def test_func_return_value():
    """
    Пробуємо створити тест всередині модуля"""
    assert type(func_for_module_import()) is str, "Функція має повертати стрічку"
