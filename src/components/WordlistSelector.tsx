import React, { SetStateAction, Dispatch } from 'react';

// TODO: MAKE WORDLIST SELECOR

const wordlists = {
  "Bitcoin's BIP 39": "/wordlists/bip_039.txt"
}

// const defaultWordlist = Object.keys(wordlists)[0]

interface IWordlistSelectorProps {
  setDictionary: Dispatch<SetStateAction<Array<string>>>
}

export const WordlistSelector: React.FunctionComponent<IWordlistSelectorProps> = (
  props: IWordlistSelectorProps
) => {
  console.log(props)

  return (
    <>
      <select>
        {
          Object.keys(wordlists).map((wordlistName) => {
            return (
              <option key={wordlistName} value={wordlistName}>
                {wordlistName}
              </option>
            )
          })
        }

      </select>
    </>
  )
}
