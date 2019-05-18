from unittest import TestCase

from passphrase_savior import Suggester, ArrayWordList


DUMMY_WORDLIST = [
    "car",
    "bike",
    "scooter",
    "skate",
    "airplane",
    "train",
]


class SuggesterTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.suggestor = Suggester(
            ArrayWordList(DUMMY_WORDLIST)
        )

        super().setUpClass()

    def test_get_similar_matches_with_prefix(self):
        self.assertEqual(
            set(self.suggestor.get_similar(
                word="bicke",
                prefix_match_lenght=2,
                allowed_lenght_delta=1,
                percentage_of_chars_to_match=70,
            )),
            {"bike"}
        )

    def test_get_similar_matches_one_without_prefix(self):
        self.assertEqual(
            set(self.suggestor.get_similar(
                word="rain",
                prefix_match_lenght=0,
                allowed_lenght_delta=1,
                percentage_of_chars_to_match=90,
            )),
            {"train"}
        )

    def test_get_similar_matches_two_without_prefix(self):
        self.assertEqual(
            set(self.suggestor.get_similar(
                word="rain",
                prefix_match_lenght=0,
                allowed_lenght_delta=1,
                percentage_of_chars_to_match=70,
            )),
            {"train", "car"}
        )

    def test_get_similar_no_matches(self):
        self.assertFalse(
            set(self.suggestor.get_similar(
                word="rain",
                prefix_match_lenght=1,
                allowed_lenght_delta=1,
                percentage_of_chars_to_match=70,
                include_word=False,
            )),
        )
