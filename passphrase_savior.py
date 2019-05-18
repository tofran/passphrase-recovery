

from abc import ABC


class WordList(ABC):
    def get_list(self):
        return self.list

    # TODO: check online on how to properlly implement in keyword
    def contains(self, obj):
        return obj in self.get_list()


class ArrayWordList(WordList):
    def __init__(self, iterable):
        self.list = list(iterable)


class MultilineStringWordList(WordList):
    def __init__(self, multiline_string):
        self.list = self._get_list(multiline_string)

    def _get_list(self, multiline_string):
        return list(
            filter(
                lambda word: word != "",
                map(lambda word: word.strip(), self.string.split("\n"))
            )
        )


class Suggester:
    DEFAULT_WORD_SEPARATOR = ""

    def __init__(
        self,
        wordlist,
        word_separator=None,

        prefix_match_lenght=2,
        allowed_lenght_delta=2,
        percentage_of_chars_to_match=70,
        include_word=False,
    ):
        self.wordlist = wordlist
        self.word_separator = self.DEFAULT_WORD_SEPARATOR if word_separator is None else word_separator

        self.prefix_match_lenght = prefix_match_lenght
        self.allowed_lenght_delta = allowed_lenght_delta
        self.percentage_of_chars_to_match = percentage_of_chars_to_match
        self.include_word = include_word

    def get_words(self, passphrase_str):
        return passphrase_str.split(self.word_separator)

    def get_variations(self, passphrase_str):
        for word in self.get_words(passphrase_str):
            yield set(self.get_similar(
                prefix_match_lenght=2,
                allowed_lenght_delta=2,
                percentage_of_chars_to_match=70,
                include_word=False,
            ))

    def get_similar(
        self,
        word,
    ):
        word_lengh = len(word)
        number_of_chars_to_match = int(
            self.percentage_of_chars_to_match/100*word_lengh
        )  # floring, should I round?

        for dictionary_word in self.wordlist.get_list():
            if dictionary_word == word:
                if self.include_word:
                    yield word
                continue

            matched_words = 0
            if (
                dictionary_word.startswith(word[:self.prefix_match_lenght]) and
                abs(
                    word_lengh-len(dictionary_word)
                ) <= self.allowed_lenght_delta
            ):
                for char in word:
                    # TODO: consider character order
                    if char in dictionary_word:
                        matched_words += 1

                if matched_words >= number_of_chars_to_match:
                    yield dictionary_word
