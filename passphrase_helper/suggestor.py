
import itertools


class Suggestor:
    DEFAULT_WORD_SEPARATOR = " "

    def __init__(
        self,
        wordlist,
        passphrase_str,

        prefix_match_lenght=2,
        allowed_lenght_delta=2,
        percentage_of_chars_to_match=70,
        word_separator=None,
    ):
        self.wordlist = wordlist

        self.prefix_match_lenght = prefix_match_lenght
        self.allowed_lenght_delta = allowed_lenght_delta
        self.percentage_of_chars_to_match = percentage_of_chars_to_match

        self.word_separator = self.DEFAULT_WORD_SEPARATOR if word_separator is None else word_separator
        self.passphrase = passphrase_str.split(self.word_separator)

    # def get_variations(self, passphrase_str):
    #     for word in self.get_words(passphrase_str):
    #         yield set(self.get_similar(word, include_itself=False))

    def suggest(self):
        for word in self.passphrase:
            yield (word, set(self.get_similar(word, include_itself=False)))

    def get_possibilities(self):
        for word in self.passphrase:
            yield set(self.get_similar(word, include_itself=True))

    def get_permutations(self):
        return itertools.product(*self.get_possibilities())  # FIXME: NOT THE PRODUCT

    def get_possible_passphrases(self):
        return map(lambda words: self.word_separator.join(words), self.get_permutations())

    def get_similar(
        self,
        word,
        include_itself=False,
    ):
        word_lengh = len(word)
        number_of_chars_to_match = int(
            self.percentage_of_chars_to_match/100*word_lengh
        )  # floring, should I round?

        for dictionary_word in self.wordlist:
            if dictionary_word == word:
                if include_itself:
                    yield word
                continue

            matched_words = 0
            if (
                dictionary_word.startswith(word[:self.prefix_match_lenght])
                and abs(
                    word_lengh-len(dictionary_word)
                ) <= self.allowed_lenght_delta
            ):
                for char in word:
                    # TODO: consider character order
                    if char in dictionary_word:
                        matched_words += 1

                if matched_words >= number_of_chars_to_match:
                    yield dictionary_word
