from unittest import TestCase

from passphrase_helper.wordlist import WordList, StrWordList


class WordListTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wordlist = WordList(["bike"])

        super().setUpClass()

    def test_contains_word_in_wordlist(self):
        self.assertTrue("bike" in self.wordlist)

    def test_contains_word_not_in_wordlist(self):
        self.assertFalse("house" in self.wordlist)

    def test_iter(self):
        i = iter(self.wordlist)

        self.assertEqual(next(i), "bike")

        with self.assertRaises(StopIteration):
            next(i)


class StrWordListTestCase(TestCase):
    def test_str_word_list_simple(self):
        self.assertEqual(
            StrWordList("bike\nboat").list,
            ["bike", "boat"],
        )

    def test_str_word_list_dirty_string(self):
        self.assertEqual(
            StrWordList("bike\nboat\n \n\nscooter\n").list,
            ["bike", "boat", "scooter"],
        )
