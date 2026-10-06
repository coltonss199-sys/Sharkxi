"""Build one candidate word list per vowel from the CMU dict.

usage: python build_candidates.py CMUDICT OUT_DIR [MIN_ZIPF]

Each OUT_DIR/<group>.tsv lists qualifying two-syllable words whose primary
stress falls on that vowel, sorted into rhyme families (same tail = perfect
rhyme) so families are easy to scan. MIN_ZIPF (default 2.8) drops rare words
when the wordfreq package is installed.
"""

import os
import sys
from collections import defaultdict

from phonetics import GROUPS, base, load_cmu, qualifying, stressed_index, tail

try:
    from wordfreq import zipf_frequency
except ImportError:  # still works, just without the rarity filter
    zipf_frequency = None


def main():
    cmu_path, out_dir = sys.argv[1], sys.argv[2]
    min_zipf = float(sys.argv[3]) if len(sys.argv) > 3 else 2.8
    os.makedirs(out_dir, exist_ok=True)
    prons = load_cmu(cmu_path)

    rows = defaultdict(list)
    for word, plist in prons.items():
        z = zipf_frequency(word, "en") if zipf_frequency else 0.0
        if zipf_frequency and z < min_zipf:
            continue
        seen = set()
        for m, p in qualifying(plist):
            v = base(p[stressed_index(p)])
            group = next((g for g, vs in GROUPS.items() if v in vs), None)
            key = (m, " ".join(p))
            if group is None or key in seen:
                continue
            seen.add(key)
            rows[group].append((" ".join(tail(p)), m, word, " ".join(p), z))

    for group in GROUPS:
        family_size = defaultdict(int)
        for t, m, *_ in rows[group]:
            family_size[(t, m)] += 1
        ordered = sorted(rows[group],
                         key=lambda r: (r[1], -family_size[(r[0], r[1])], r[0], -r[4]))
        path = os.path.join(out_dir, f"{group}.tsv")
        with open(path, "w", encoding="utf-8") as f:
            f.write("word\tmeter\tpronunciation\trhyme_tail\tzipf\n")
            for t, m, word, p, z in ordered:
                f.write(f"{word}\t{m}\t{p}\t{t}\t{z:.2f}\n")
        print(f"{group:8s} {len(rows[group]):5d} candidates -> {path}")


if __name__ == "__main__":
    main()
