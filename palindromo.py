import unittest

def palindrome(word):
    return True

class TestPalindrome(unittest.TestCase):

    def test_palindrome_simple(self):

        result = palindrome('neuquen')

        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()

