
from itertools import product


class Suggestor:
    DEFAULT_WORD_SEPARATOR = " "

    def __init__(
        self,
        wordlist,
        passphrase_str,

        prefix_match_lenght,
        allowed_lenght_delta,
        percentage_of_chars_to_match,
        word_separator,
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

    def get_invalid(self):
        return [word for word in self.passphrase if word not in self.wordlist]

    def suggest(self, only_errors=False):
        for word in self.passphrase:
            if not only_errors or word not in self.wordlist:
                yield (word, self.get_similar(word, include_itself=False))

    def get_possibilities(self):
        for word in self.passphrase:
            yield self.get_similar(word, include_itself=True)

    def get_permutations(self):
        return product(*self.get_possibilities())

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

            matched_chars = 0
            if (
                dictionary_word.startswith(word[:self.prefix_match_lenght])
                and abs(
                    word_lengh-len(dictionary_word)
                ) <= self.allowed_lenght_delta
            ):
                for char in word:
                    # TODO: consider character order
                    if char in dictionary_word:
                        matched_chars += 1

                if matched_chars >= number_of_chars_to_match:
                    yield dictionary_word
