

ALWAYS_STARTS_WITH_KNOWN_LETTER = True
MAX_LENGHT_VARIATION = 1
FOUND_CHARS_LENGHT_MULTI = 0.9

WORD_SEPARATOR = ' '

dictionary = []

with open('bip_039_wordlist.txt', 'r') as dictionary_file:
    for line in dictionary_file:
        dictionary.append(line.strip())

print("Loaded {} words".format(len(dictionary)))

known_passphrase = None
if not known_passphrase:
    known_passphrase = input('Input the known passphrase: ')

known_words = known_passphrase.split(WORD_SEPARATOR)

print("Looking for passphrases similar to: {}\n".format(known_words))

for word in known_words:
    word_lengh = len(word)
    score_needed = int(FOUND_CHARS_LENGHT_MULTI*word_lengh)
    possible_matches = []
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
