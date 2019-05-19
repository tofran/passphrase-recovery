
class Suggestor:
    DEFAULT_WORD_SEPARATOR = " "

    def __init__(
        self,
        wordlist,
        word_separator=None,

        prefix_match_lenght=2,
        allowed_lenght_delta=2,
        percentage_of_chars_to_match=70,
        include_itself=False,
    ):
        self.wordlist = wordlist
        self.word_separator = self.DEFAULT_WORD_SEPARATOR if word_separator is None else word_separator

        self.prefix_match_lenght = prefix_match_lenght
        self.allowed_lenght_delta = allowed_lenght_delta
        self.percentage_of_chars_to_match = percentage_of_chars_to_match
        self.include_itself = include_itself

    def get_words(self, passphrase_str):
        return passphrase_str.split(self.word_separator)

    def get_variations(self, passphrase_str):
        for word in self.get_words(passphrase_str):
            yield set(self.get_similar(word))

    def get_similar(
        self,
        word,
    ):
        word_lengh = len(word)
        number_of_chars_to_match = int(
            self.percentage_of_chars_to_match/100*word_lengh
        )  # floring, should I round?

        for dictionary_word in self.wordlist:
            if dictionary_word == word:
                if self.include_itself:
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
