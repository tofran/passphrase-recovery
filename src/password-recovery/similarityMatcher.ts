import levenshtein from "levenshtein-edit-distance";


interface IWordSimilarity {
  word: string,
  diff: number,
}

export interface ISimilarityMatcherSettings {
  maxDiff: number,
  maxSuggestions?: number,
}

export interface ISimilarityMatcherArgs extends ISimilarityMatcherSettings {
  word: string,
  wordlist: Array<string>,
}

export const getSimilarities = (
  {
    word,
    wordlist,
    maxDiff,
    maxSuggestions,
  }: ISimilarityMatcherArgs
): Array<IWordSimilarity> => {

  const similarities = wordlist
    .map(wordlistWord => (
      {
        word: wordlistWord,
        diff: levenshtein(word, wordlistWord),
      }
    ))
    .filter(suggestion => (
      suggestion.word !== word
      && suggestion.diff <= maxDiff
    ))

  if (maxSuggestions) {
    return similarities.slice(0, maxSuggestions)
  }

  return similarities
}

export const getSimilarWords = (
  args: ISimilarityMatcherArgs
): Array<string> => (
    getSimilarities(args)
      .map(({ word }) => word)
  )