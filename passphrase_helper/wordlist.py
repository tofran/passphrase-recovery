

from abc import ABC


class WordList(ABC):
    def __init__(self, list):
        self.list = list

    def __iter__(self):
        return iter(self.list)

    def __contains__(self, item):
        return item in self.list


class StrWordList(WordList):
    def __init__(self, input_str):
        self.list = self.make_list(input_str.split("\n"))

    def make_list(self, iterable):
        return list(
            filter(
                lambda word: word != "",
                map(lambda word: word.strip(), iterable)
            )
        )


class FileWordlist(StrWordList):
    def __init__(self, filenpath):
        with open(filenpath, "r") as f:
            self.list = self.make_list(f)
