

ALWAYS_STARTS_WITH_KNOWN_LETTER = True
MAX_LENGHT_VARIATION = 1
FOUND_CHARS_LENGHT_MULTI = 0.9
KNOWN_PASSPHRASE = None
PASSPHRASE_LENGHT = None

WORD_SEPARATOR = ' '

dictionary = []

with open('bip_039_wordlist.txt', 'r') as dictionary_file:
    for line in dictionary_file:
        dictionary.append(line.strip())

print("Loaded {} words".format(len(dictionary)))

if not KNOWN_PASSPHRASE:
    KNOWN_PASSPHRASE = input('Input the known passphrase: ')

known_words = KNOWN_PASSPHRASE.split(WORD_SEPARATOR)

if PASSPHRASE_LENGHT and len(known_words) != PASSPHRASE_LENGHT:
    raise ValueError(
        "Expected {} words, got {}".format(
            PASSPHRASE_LENGHT,
            len(known_words),
        )
    )

print(
    "Looking for passphrases similar to: {}\n".format(known_words)
)

for word in known_words:
    word_lengh = len(word)
    score_needed = int(FOUND_CHARS_LENGHT_MULTI*word_lengh)
    possible_matches = []

    if word not in dictionary:
        raise RuntimeError(
            "The word '{}' is not in the dictonary".format(
                word,
            )
        )

    for dictionary_word in dictionary:
        score = 0
        if (
            ALWAYS_STARTS_WITH_KNOWN_LETTER and
            dictionary_word.startswith(word[0]) and
            dictionary_word != word and
            abs(word_lengh-len(dictionary_word)) <= MAX_LENGHT_VARIATION
        ):
            for char in word:
                if char in dictionary_word:
                    score += 1
            if score >= score_needed:
                possible_matches.append(dictionary_word)

    print(
        "{} can be: {}".format(
            word,
            possible_matches,
        )
    )
