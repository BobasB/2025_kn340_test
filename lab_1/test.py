import unittest
from unittest.mock import patch
from main import *

class TestWordChoice(unittest.TestCase):
    def test_choose_secret_word(self):
        self.assertIn(choose_secret_word(WORDS), WORDS)
    
    def test_empty_list(self):
        with self.assertRaises(IndexError):
            choose_secret_word([])

class TestEnterLetterFromUser(unittest.TestCase):
    @patch('builtins.input', side_effect=['2', 'a'])
    def test_enter_letter_from_user(self, mock_input):
        self.assertEqual(enter_letter_from_user(), '2')
        self.assertEqual(enter_letter_from_user(), 'a')

        # __builtins__.input = mock_input
        # try:
        #     self.assertEqual(enter_letter_from_user(), 'a')
        # finally:
        #     __builtins__.input = original_input

class TestCheckLettersInWord(unittest.TestCase):
    def test_all_letters_guessed(self):
        """
        Даний тест є валідним, тому ми його трохи переписали."""
        test_word = 'apple'
        self.assertEqual(
            check_letters_in_word(set(test_word), test_word),
            test_word
        )

    def test_no_letters_guessed(self):
        self.assertEqual(
            check_letters_in_word(set(), 'banana'),
            '******'
        )

    def test_some_letters_guessed(self):
        self.assertEqual(
            check_letters_in_word({'a', 'n'}, 'banana'),
            '*anana'
        )

    def test_repeated_letters(self):
        self.assertEqual(
            check_letters_in_word({'b', 'a'}, 'banana'),
            'ba*a*a'
        )

    def test_empty_word(self):
        """
        Даний тест ми залишимо, але трохи модифікуємо."""
        guess_letter = set("")
        # Виловлюємо помилку
        with self.assertRaises(ValueError):
            check_letters_in_word(guess_letter, "")
        # Перевіряємо текст помилки, що це саме наша помилка яку ми написали
        with self.assertRaises(ValueError) as context:
            check_letters_in_word(guess_letter, "")
            self.assertEqual(str(context.exception), "Word cannot be empty")

    
    def test_empty_letters(self):
        """
        Даний тест ми також залишимо та трохи модифікуємо.
        Допишемо на наступний раз."""
        test_word = 'test'
        guess_letter = set("")
        
    
        # self.assertIsInstance(guess_letter, set)
        # self.assertEqual(
        #     check_letters_in_word(set(""), test_word),
        #     ''
        # )


if __name__ == "__main__":
    unittest.main(verbosity=2)
