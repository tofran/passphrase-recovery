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
  ) => (
        setSimilarityMatcherSettings({
          ...similarityMatcherSettings,
          [settingName]: event.target.value
        })
      )


  return (
    <form>
      <label>
        Max difference:
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
          min="-1"
          value={similarityMatcherSettings.maxSuggestions}
          onChange={handleInputChange("maxSuggestions")} />
      </label>
    </form>
  )
}