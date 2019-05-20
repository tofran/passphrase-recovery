import argparse

from suggestor import Suggestor
from wordlist import FileWordlist

DEFAULT_WORDLIST_PATH = "../bip_039_wordlist.txt"


def main():
    parser = argparse.ArgumentParser(description="Passphrase typo fixer and helper")

    parser.add_argument("known_passphrase", type=str, help="The passphrase that is known")
    parser.add_argument(
        "--list",
        action="store_true",
        default=False,
        help="List all the combinations",
    )
    parser.add_argument(
        "word-separator",
        type=str,
        nargs="?",
        default=" ",
        help="Word separator",
    )
    parser.add_argument(
        "--wordlist",
        type=str,
        help="Path to the wordlist",
        default=DEFAULT_WORDLIST_PATH,
    )

    args = parser.parse_args()
    suggestor = Suggestor(
        wordlist=FileWordlist(args.wordlist),
        passphrase_str=args.known_passphrase,
    )

    if args.list:
        print("\n".join(suggestor.get_possible_passphrases()))

    else:
        for word, suggestions in suggestor.suggest():
            print("{:10}: {}".format(
                word,
                ", ".join(list(suggestions)),
            ))


if __name__ == "__main__":
    main()
