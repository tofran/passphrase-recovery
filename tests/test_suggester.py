from unittest import TestCase

from passphrase_helper.suggestor import Suggestor
from passphrase_helper.wordlist import WordList


DUMMY_WORDLIST = [
    "car",
    "bike",
    "scooter",
    "skate",
    "airplane",
    "train",
]


class SuggestorTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wordlist = WordList(DUMMY_WORDLIST)

        super().setUpClass()

    def test_get_similar_matches_with_prefix(self):
        sugestor = Suggestor(
            self.wordlist,
            prefix_match_lenght=2,
            allowed_lenght_delta=1,
            percentage_of_chars_to_match=70,
            include_itself=False,
        )

        self.assertEqual(
            set(sugestor.get_similar("bicke")),
            {"bike"}
        )

    def test_get_similar_matches_one_without_prefix(self):
        sugestor = Suggestor(
            self.wordlist,
            prefix_match_lenght=0,
            allowed_lenght_delta=1,
            percentage_of_chars_to_match=90,
            include_itself=False,
        )

        self.assertEqual(
            set(sugestor.get_similar("rain")),
            {"train"}
        )

    def test_get_similar_matches_two_without_prefix(self):
        sugestor = Suggestor(
            self.wordlist,
            prefix_match_lenght=0,
            allowed_lenght_delta=1,
            percentage_of_chars_to_match=70,
            include_itself=False,
        )

        self.assertEqual(
            set(sugestor.get_similar("rain")),
            {"train", "car"}
        )

    def test_get_similar_no_matches(self):
        sugestor = Suggestor(
            self.wordlist,
            prefix_match_lenght=1,
            allowed_lenght_delta=1,
            percentage_of_chars_to_match=70,
            include_itself=False,
        )

        self.assertFalse(
            set(sugestor.get_similar("rain")),
        )
