import bip_039_en from './wordlists/bip_039_en'

interface IWordlist {
  name: string,
  wordlist: Array<string>,
}

export const bip039: IWordlist = {
  name: "Bitcoin's BIP: 39 - English",
  wordlist: bip_039_en,
}
