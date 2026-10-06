# Rhyme pairs

Semantically related rhyme pairs mined from the CMU Pronouncing Dictionary.
The result is [`RHYME_PAIRS.md`](RHYME_PAIRS.md) (also as [`rhyme_pairs.csv`](rhyme_pairs.csv)).

## Rebuilding

```sh
curl -sSfLo cmudict.dict https://raw.githubusercontent.com/cmusphinx/cmudict/master/cmudict.dict
pip install wordfreq                                 # optional: drops rare words

python build_candidates.py cmudict.dict candidates 3.0   # one word list per vowel
# ...pick pairs into results/<vowel>.tsv and results/<vowel>_nearmisses.tsv...
python validate.py cmudict.dict long_a results/long_a.tsv --expect 100
python assemble.py cmudict.dict results .
```

`results/` holds the ten per-vowel lists, as picked by one agent per vowel, so
`assemble.py` can be re-run without redoing the search.

- `phonetics.py` holds the rules: syllable count, iamb/trochee meter, r/l-controlled
  syllables, and the perfect / slant / assonance classifier.
- `build_candidates.py` writes the words that pass those rules, grouped by stressed vowel
  and sorted into perfect-rhyme families.
- `validate.py` checks a pairs file against CMU, including that each rhyme label is the
  one the phonemes support.
- `assemble.py` re-validates all ten files, rejects cross-vowel duplicates, and writes the
  Markdown and CSV.
