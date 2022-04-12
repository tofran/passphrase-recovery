import bip_039_czech from './wordlists/bip_039_czech'
import bip_039_english from './wordlists/bip_039_english'
import bip_039_french from './wordlists/bip_039_french'
import bip_039_italian from './wordlists/bip_039_italian'
import bip_039_japanese from './wordlists/bip_039_japanese'
import bip_039_korean from './wordlists/bip_039_korean'
import bip_039_portuguese from './wordlists/bip_039_portuguese'
import bip_039_spanish from './wordlists/bip_039_spanish'

interface IWordlist {
  id: string,
  name: string,
  wordlist: Array<string>,
}

export const wordlists: IWordlist[] = [
  {
    id: "bip_039_english",
    wordlist: bip_039_english,
    name: "Bitcoin's BIP039 - English",
  },
  {
    id: "bip_039_czech",
    wordlist: bip_039_czech,
    name: "Bitcoin's BIP039 - Czech",
  },
  {
    id: "bip_039_french",
    wordlist: bip_039_french,
    name: "Bitcoin's BIP039 - French",
  },
  {
    id: "bip_039_italian",
    wordlist: bip_039_italian,
    name: "Bitcoin's BIP039 - Italian",
  },
  {
    id: "bip_039_japanese",
    wordlist: bip_039_japanese,
    name: "Bitcoin's BIP039 - Japanese",
  },
  {
    id: "bip_039_korean",
    wordlist: bip_039_korean,
    name: "Bitcoin's BIP039 - Korean",
  },
  {
    id: "bip_039_portuguese",
    wordlist: bip_039_portuguese,
    name: "Bitcoin's BIP039 - Portuguese",
  },
  {
    id: "bip_039_spanish",
    wordlist: bip_039_spanish,
    name: "Bitcoin's BIP039 - Spanish",
  }
]
