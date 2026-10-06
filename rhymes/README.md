# Rhyme pairs

Rhyme pairs mined from the CMU Pronouncing Dictionary where the words are also
related in meaning. The result is [`RHYME_PAIRS.md`](RHYME_PAIRS.md), also
available as [`rhyme_pairs.csv`](rhyme_pairs.csv). Each vowel's raw picks and
near-misses are in `results/`.

## Rebuilding

```sh
curl -sSfLo cmudict.dict https://raw.githubusercontent.com/cmusphinx/cmudict/master/cmudict.dict
pip install wordfreq                                    # optional: drops rare words

python build_candidates.py cmudict.dict candidates 3.0 3   # one word list per vowel
python lookup.py cmudict.dict glow                         # rhymes for a word
python lookup.py cmudict.dict --pair grace praise          # rhyme type of a pair
# ...pick pairs into results/<vowel>.tsv and results/<vowel>_nearmisses.tsv...
python validate.py cmudict.dict long_a results/long_a.tsv --expect 100 \
    --misses results/long_a_nearmisses.tsv
python assemble.py cmudict.dict results .
```

- `phonetics.py` holds the rules: the r/l-controlled syllable test and the
  perfect / slant / assonance classifier.
- `build_candidates.py` writes the common words that pass those rules. It groups
  them by stressed vowel and sorts them into perfect-rhyme families.
- `lookup.py` lists a word's qualifying rhymes, or classifies a single pair.
- `validate.py` checks a pairs file against CMU, including that each rhyme label
  is the one the phonemes support.
- `assemble.py` re-validates all ten files, rejects pairs that appear under two
  vowels, and writes the Markdown and CSV.
