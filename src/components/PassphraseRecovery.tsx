import React, { useState } from 'react';
import { ISimilarityMatcherSettings } from '~/password-recovery/similarityMatcher';
import { bip039 } from '~/password-recovery/wordlists';
import { PassphraseWord } from './PassphraseWord';
import { MatcherSettings } from './Settings';


const wordlist = bip039.wordlist;

export const PassphraseRecovery: React.FunctionComponent = () => {
  const [passphrase, setPassphrase] = useState<string[]>()


  const [
    similarityMatcherSettings, setSimilarityMatcherSettings
  ] = React.useState<ISimilarityMatcherSettings>({
    maxDiff: 2,
    maxSuggestions: -1
  })

  const updateInputWords = (input: HTMLTextAreaElement) => {
    const newPassphrase = (
      input.value
        .replaceAll("\n", " ")
        .split(" ")
        .map((word) => (
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
      <textarea
        placeholder="Type your misspelled passphrease"
        onChange={onInputChange}
        rows={6}
      >
      </textarea>

      <p>
        {
          wordlist
            ? `Loaded ${wordlist.length} words from the worlist.`
            : `Loading wordlist...`
        }
      </p>

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
