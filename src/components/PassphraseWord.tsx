import React from 'react';
import { ISimilarityMatcherSettings, getSimilarities } from '~/password-recovery/similarityMatcher';

interface IPassphraseWordProps {
  word: string,
  wordlist: Array<string>,
  similarityMatcherSettings: ISimilarityMatcherSettings,
}

export const PassphraseWord: React.FunctionComponent<IPassphraseWordProps> = (
  {
    word,
    wordlist,
    similarityMatcherSettings,
  }: IPassphraseWordProps
) => {

  const wordExists = wordlist.includes(word)

  return <li>
    <span
      className={
        wordExists
          ? ""
          : "error"
      }
      title={
        wordExists
          ? ""
          : "This word may be misspelled, it is not int he selected wordlist"
      }
    >
      {word}
    </span>

    <ol>
      {
        getSimilarities({
          word: word,
          wordlist: wordlist,
          ...similarityMatcherSettings,
        })
          .map(({ word, diff }) => (
            <li key={word}>
              {word} ({diff});
            </li>
          ))
      }
    </ol>
  </li>
}
