import React, { Dispatch, SetStateAction } from 'react';
import { ISimilarityMatcherSettings } from '~/password-recovery/similarityMatcher';


interface IMatcherSettingsProps {
  similarityMatcherSettings: ISimilarityMatcherSettings,
  setSimilarityMatcherSettings: Dispatch<SetStateAction<ISimilarityMatcherSettings>>,
}

export const MatcherSettings: React.FunctionComponent<IMatcherSettingsProps> = (
  {
    similarityMatcherSettings,
    setSimilarityMatcherSettings,
  }: IMatcherSettingsProps
) => {

  const handleInputChange = (
    settingName: string
  ) => (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
      setSimilarityMatcherSettings({
        ...similarityMatcherSettings,
        [settingName]: parseInt(event.target.value),
      })
    }

  return (
    <form>
      <label>
        Max word distance
        (<a href='https://en.wikipedia.org/wiki/Levenshtein_distance'>Levenshtein distance</a>):
        <input
          type="number"
          min="0"
          value={similarityMatcherSettings.maxDiff}
          onChange={handleInputChange("maxDiff")} />
      </label>

      <label>
        Max suggestions per word:
        <input
          type="number"
          min="0"
          value={similarityMatcherSettings.maxSuggestions}
          onChange={handleInputChange("maxSuggestions")} />
      </label>
    </form>
  )
}