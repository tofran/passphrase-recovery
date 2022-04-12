import React, { useState } from 'react';
import { ISimilarityMatcherSettings } from '~/password-recovery/similarityMatcher';
import { wordlists } from '~/password-recovery/wordlists';
import { PassphraseWord } from './PassphraseWord';
import { MatcherSettings } from './Settings';
import { WordlistSelector } from './WordlistSelector';

export const PassphraseRecovery: React.FunctionComponent = () => {
  const [passphrase, setPassphrase] = useState<string[]>()
  const [wordlist, setWordlist] = useState<string[]>(wordlists[0].wordlist)

  const [
    similarityMatcherSettings, setSimilarityMatcherSettings
  ] = React.useState<ISimilarityMatcherSettings>({
    maxDiff: 2,
    maxSuggestions: 99
  })

  const updateInputWords = (input: HTMLTextAreaElement) => {
    const newPassphrase = (
      input.value
        .replaceAll("\n", " ")
        .split(" ")
        .map(word => (
          word
            .trim()
            .toLowerCase()
        ))
        .filter((word) => word)
    )

    setPassphrase(newPassphrase)
  }

  const onInputChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    updateInputWords(event.target)
  }

  return (
    <>
      <WordlistSelector setWordlist={setWordlist}/>
      <span>{`Loaded ${wordlist.length} words from the worlist.`}</span>

      <textarea
        placeholder="Type your misspelled passphrase..."
        onChange={onInputChange}
        rows={6}
      >
      </textarea>

      <MatcherSettings
        similarityMatcherSettings={similarityMatcherSettings}
        setSimilarityMatcherSettings={setSimilarityMatcherSettings}
      />

      {
        passphrase &&
        <ol>
          {passphrase.map((word, index) => (
            <PassphraseWord
              key={`${index}-${word}`}
              word={word}
              wordlist={wordlist}
              similarityMatcherSettings={{
                ...similarityMatcherSettings,
                maxSuggestions: (
                  similarityMatcherSettings.maxSuggestions == -1
                    ? undefined
                    : similarityMatcherSettings.maxSuggestions
                ),
              }}
            />
          ))}
        </ol>
      }
    </>
  )
}
