import unittest
from unittest.mock import patch
from main import choose_secret_word, enter_letter_from_user, WORDS

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
    

if __name__ == "__main__":
    unittest.main(verbosity=2)
