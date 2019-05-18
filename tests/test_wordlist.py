from unittest import TestCase

from passphrase_savior import ArrayWordList


class WordListTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wordlist = ArrayWordList(["bike"])

        super().setUpClass()

    def test_word_in_wordlist(self):
        self.assertTrue(
            self.wordlist.contains("bike")
        )

    def test_word_not_in_wordlist(self):
        self.assertFalse(
            self.wordlist.contains("house")
        )
