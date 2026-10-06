"""Merge the per-vowel results into RHYME_PAIRS.md and rhyme_pairs.csv.

usage: python assemble.py CMUDICT RESULTS_DIR OUT_DIR

Re-validates every <group>.tsv and its near-misses before writing, and
refuses to assemble if any file fails or a pair appears under two vowels.
"""

import csv
import os
import sys
from collections import Counter

from phonetics import GROUPS, load_cmu
from validate import check, check_misses, read_tsv

TITLES = {
    "long_a": ("Long A", "/eɪ/", "EY", "brave, grace"),
    "long_e": ("Long E", "/iː/", "IY", "free, peace"),
    "long_i": ("Long I", "/aɪ/", "AY", "bright, shine"),
    "long_o": ("Long O", "/oʊ/", "OW", "glow, hope"),
    "long_u": ("Long U", "/uː/, /juː/", "UW", "true, music"),
    "short_a": ("Short A", "/æ/", "AE", "glad, laugh"),
    "short_e": ("Short E", "/ɛ/", "EH", "best, fresh"),
    "short_i": ("Short I", "/ɪ/", "IH", "gift, sing"),
    "short_o": ("Short O", "/ɑ/, /ɔ/", "AA, AO", "top, song"),
    "short_u": ("Short U", "/ʌ/", "AH", "sun, love"),
}
LINK_NAMES = {"synonym": "Synonym", "antonym": "Antonym", "cause-effect": "Cause/effect",
              "part-whole": "Part/whole", "scene": "Same scene"}


def cell(text):
    return text.strip().replace("|", "\\|")


def main():
    cmu_path, results_dir, out_dir = sys.argv[1:4]
    prons = load_cmu(cmu_path)

    data, failures = {}, []
    for group in GROUPS:
        _, rows = read_tsv(os.path.join(results_dir, f"{group}.tsv"))
        _, misses = read_tsv(os.path.join(results_dir, f"{group}_nearmisses.tsv"))
        problems = check(prons, group, rows) + check_misses(misses)
        if len(rows) != 100:
            problems.append(f"expected 100 rows, found {len(rows)}")
        failures += [f"{group}: {p}" for p in problems]
        data[group] = (rows, misses)

    owner = {}
    for group, (rows, _) in data.items():
        for r in rows:
            key = tuple(sorted((r["word1"].lower(), r["word2"].lower())))
            if key in owner:
                failures.append(f"{group}: {key} already listed under {owner[key]}")
            owner.setdefault(key, group)
    if failures:
        print("\n".join(failures))
        sys.exit(1)

    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "rhyme_pairs.csv"), "w",
              encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["vowel", "rank", "word1", "word2", "rhyme_type", "link",
                    "relationship", "example"])
        for group, (rows, _) in data.items():
            for r in rows:
                w.writerow([group] + [r[c].strip() for c in
                                      ("rank", "word1", "word2", "rhyme_type", "link",
                                       "relationship", "example")])

    total = sum(len(rows) for rows, _ in data.values())
    out = [
        "# Rhyme Pairs That Mean Something",
        "",
        f"{total} rhyme pairs where the sound link reinforces a meaning link, mined "
        "from the [CMU Pronouncing Dictionary](https://github.com/cmusphinx/cmudict). "
        "There are 100 per vowel, from one search agent for each long and short vowel.",
        "",
        "**`validate.py` checked every pair against CMU:**",
        "",
        "- no r- or l-controlled syllables in either word (no ER, no vowel closed by "
        "R or L). An L or R that starts a syllable is fine (*bright*, *glow*, *delight*);",
        "- the first word carries primary stress on the section's vowel;",
        "- the rhyme type is the one CMU's phonemes actually support: "
        "**perfect** (identical from the stressed vowel on), **slant** "
        "(one or two near-consonant swaps, or a different vowel over identical "
        "endings), or **assonance** (same stressed vowel only);",
        "- the relationship is 3-5 words and the example line uses both words.",
        "",
        "The agents made the editorial calls: the meaning links, keeping words "
        "positive, and ranking (strongest sound and sense first). Each section ends "
        "with five near-misses that were rejected.",
        "",
        "| Vowel | Pairs | Perfect | Slant | Assonance |",
        "|---|---|---|---|---|",
    ]
    for group, (rows, _) in data.items():
        c = Counter(r["rhyme_type"].strip().lower() for r in rows)
        name, ipa, *_ = TITLES[group]
        out.append(f"| [{name} {ipa}](#{name.lower().replace(' ', '-')}) | {len(rows)} "
                   f"| {c['perfect']} | {c['slant']} | {c['assonance']} |")

    for group, (rows, misses) in data.items():
        name, ipa, cmu, example = TITLES[group]
        out += ["", f"## {name}", "",
                f"{ipa} as in *{example}*: CMU `{cmu}` under primary stress.", "",
                "| # | Pair | Rhyme type | Relationship | One-line example use |",
                "|---|---|---|---|---|"]
        for r in rows:
            pair = f"**{cell(r['word1'])}** / **{cell(r['word2'])}**"
            link = LINK_NAMES[r["link"].strip().lower()]
            out.append(f"| {r['rank'].strip()} | {pair} | {r['rhyme_type'].strip().lower()} "
                       f"| *{link}:* {cell(r['relationship'])} | {cell(r['example'])} |")
        out += ["", f"**Near-misses rejected ({name})**", ""]
        out += [f"{i}. **{cell(m['pair'])}**: {cell(m['reason'])}"
                for i, m in enumerate(misses, start=1)]

    with open(os.path.join(out_dir, "RHYME_PAIRS.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print(f"wrote {total} pairs to {out_dir}/RHYME_PAIRS.md and rhyme_pairs.csv")


if __name__ == "__main__":
    main()
