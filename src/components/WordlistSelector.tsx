import React, { SetStateAction, Dispatch } from 'react';
import { wordlists } from '~/password-recovery/wordlists';

interface IWordlistSelectorProps {
  setWordlist: Dispatch<SetStateAction<Array<string>>>
}

export const WordlistSelector: React.FunctionComponent<IWordlistSelectorProps> = (
  {setWordlist: setWordlist}: IWordlistSelectorProps
) => {
  const onWordlistChange = ({target: select}: React.ChangeEvent<HTMLSelectElement>) => {
    const wordlistId = select.options[select.selectedIndex].id
    setWordlist(wordlists.find(wordlist => wordlist.id == wordlistId)?.wordlist || [])
  }

  return (
    <>
      <select onChange={onWordlistChange}>
        {
          wordlists.map((wordlist) => {
            return (
              <option key={wordlist.id} id={wordlist.id} value={wordlist.name} >
                {wordlist.name}
              </option>
            )
          })
        }

      </select>
    </>
  )
}
