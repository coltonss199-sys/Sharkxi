"""Look up words in the CMU dict and list their qualifying rhymes.

usage: python lookup.py CMUDICT WORD [WORD ...] [--min-zipf Z]
       python lookup.py CMUDICT --pair WORD1 WORD2

For each WORD: its pronunciations, whether it passes the r/l rule, its vowel
group, and the common qualifying words that make a perfect or slant rhyme with
it. With --pair, prints the rhyme type CMU supports for that pair.
"""

import sys

from phonetics import GROUPS, base, load_cmu, qualifying, rhyme_type, stressed_index, tail

try:
    from wordfreq import zipf_frequency
except ImportError:
    zipf_frequency = None

ORDER = {"perfect": 0, "slant": 1, "assonance": 2}


def group_of(p):
    v = base(p[stressed_index(p)])
    return next((g for g, vs in GROUPS.items() if v in vs), None)


def best(q1, q2):
    found = None
    for a in q1:
        for b in q2:
            t = rhyme_type(a, b)
            if t and (found is None or ORDER[t] < ORDER[found]):
                found = t
    return found


def main():
    args = sys.argv[1:]
    min_zipf = 3.0
    if "--min-zipf" in args:
        i = args.index("--min-zipf")
        min_zipf = float(args[i + 1])
        del args[i:i + 2]
    prons = load_cmu(args[0])
    words = [w.lower() for w in args[1:]]

    if words and words[0] == "--pair":
        w1, w2 = words[1], words[2]
        for w in (w1, w2):
            if w not in prons:
                sys.exit(f"{w}: not in CMU dict")
        q1, q2 = qualifying(prons[w1]), qualifying(prons[w2])
        if not q1 or not q2:
            sys.exit(f"{w1}/{w2}: a word breaks the r/l rule")
        print(f"{w1} / {w2}: {best(q1, q2) or 'no qualifying sound link'}")
        return

    common = {}
    for w, plist in prons.items():
        if zipf_frequency and zipf_frequency(w, "en") < min_zipf:
            continue
        q = qualifying(plist)
        if q:
            common[w] = q

    for word in words:
        if word not in prons:
            print(f"{word}: not in CMU dict\n")
            continue
        print(f"{word}:")
        for p in prons[word]:
            ok = p in qualifying(prons[word])
            tag = f"ok, {group_of(p)}" if ok else "BREAKS r/l rule (or no stress)"
            print(f"  {' '.join(p):30s} {tag}")
        q = qualifying(prons[word])
        if not q:
            print()
            continue
        perfect, slant = [], []
        for w, qw in common.items():
            if w == word:
                continue
            t = best(q, qw)
            if t == "perfect":
                perfect.append(w)
            elif t == "slant":
                slant.append(w)
        print(f"  perfect: {', '.join(sorted(perfect)) or '-'}")
        print(f"  slant:   {', '.join(sorted(slant)) or '-'}\n")


if __name__ == "__main__":
    main()
