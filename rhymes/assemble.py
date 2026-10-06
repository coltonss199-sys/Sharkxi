"""Merge the per-vowel results into RHYME_PAIRS.md and rhyme_pairs.csv.

usage: python assemble.py CMUDICT RESULTS_DIR OUT_DIR

Re-validates every <group>.tsv before writing, and refuses to assemble if
any file fails or a pair appears under two vowels.
"""

import csv
import os
import sys
from collections import Counter

from phonetics import GROUPS, load_cmu
from validate import check

TITLES = {
    "long_a": ("Long A", "/eɪ/", "EY", "brave, grateful"),
    "long_e": ("Long E", "/iː/", "IY", "peaceful, dreamy"),
    "long_i": ("Long I", "/aɪ/", "AY", "delight, shining"),
    "long_o": ("Long O", "/oʊ/", "OW", "glowing, hopeful"),
    "long_u": ("Long U", "/uː/, /juː/", "UW", "music, balloon"),
    "short_a": ("Short A", "/æ/", "AE", "happy, gladly"),
    "short_e": ("Short E", "/ɛ/", "EH", "festive, blessing"),
    "short_i": ("Short I", "/ɪ/", "IH", "wisdom, gifted"),
    "short_o": ("Short O", "/ɑ/, /ɔ/", "AA, AO", "honest, softly"),
    "short_u": ("Short U", "/ʌ/", "AH", "sunny, lovely"),
}


def read_tsv(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def cell(text):
    return text.strip().replace("|", "\\|")


def main():
    cmu_path, results_dir, out_dir = sys.argv[1:4]
    prons = load_cmu(cmu_path)

    data, failures = {}, []
    for group in GROUPS:
        rows = read_tsv(os.path.join(results_dir, f"{group}.tsv"))
        problems = check(prons, group, rows)
        if len(rows) != 100:
            problems.append(f"expected 100 rows, found {len(rows)}")
        failures += [f"{group}: {p}" for p in problems]
        misses = read_tsv(os.path.join(results_dir, f"{group}_nearmisses.tsv"))
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
        w.writerow(["vowel", "rank", "word1", "meter1", "word2", "meter2",
                    "rhyme_type", "relationship", "example"])
        for group, (rows, _) in data.items():
            for r in rows:
                w.writerow([group, r["rank"], r["word1"], r["meter1"], r["word2"],
                            r["meter2"], r["rhyme_type"], r["relationship"].strip(),
                            r["example"].strip()])

    total = sum(len(rows) for rows, _ in data.values())
    out = [
        "# Rhyme Pairs That Mean Something",
        "",
        f"{total} two-syllable rhyme pairs where the sound link reinforces a meaning "
        "link, mined from the [CMU Pronouncing Dictionary]"
        "(https://github.com/cmusphinx/cmudict) — 100 per vowel, one search agent "
        "per long and short vowel.",
        "",
        "**Every pair was machine-checked against CMU** (`validate.py`):",
        "",
        "- both words are two syllables in every CMU pronunciation (so no "
        "cov-ring / co-ver-ing ambiguity), labelled **iamb** (da-DUM) or "
        "**trochee** (DUM-da) exactly as CMU stresses them;",
        "- no r- or l-controlled syllables: no ER, no vowel closed by R or L, "
        "no syllabic -le, no silent-L spelling (talk, calm), no suffixed "
        "base-final L (roll-ing, feel-ing), and no vowel letter closed by R "
        "in the spelling (sur-prise);",
        "- the rhyme type is the one CMU's phonemes actually support — "
        "**perfect** (identical from the stressed vowel on), **slant** "
        "(one or two near-consonant swaps, or a different vowel over identical "
        "endings), or **assonance** (same stressed vowel only).",
        "",
        "Meaning links, positivity, and ranking (strongest sound + sense first) "
        "are editorial judgments by the agents. Each section ends with five "
        "near-misses that were rejected.",
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
                f"{ipa} as in *{example}* — CMU `{cmu}` under primary stress.", "",
                "| # | Pair | Rhyme type | Relationship | One-line example use |",
                "|---|---|---|---|---|"]
        for r in rows:
            pair = (f"**{cell(r['word1'])}** ({r['meter1'].strip()}) / "
                    f"**{cell(r['word2'])}** ({r['meter2'].strip()})")
            out.append(f"| {r['rank'].strip()} | {pair} | {r['rhyme_type'].strip()} "
                       f"| {cell(r['relationship'])} | {cell(r['example'])} |")
        out += ["", f"**Near-misses rejected ({name})**", ""]
        out += [f"{i}. **{cell(m['pair'])}** — {cell(m['reason'])}"
                for i, m in enumerate(misses, start=1)]

    with open(os.path.join(out_dir, "RHYME_PAIRS.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print(f"wrote {total} pairs to {out_dir}/RHYME_PAIRS.md and rhyme_pairs.csv")


if __name__ == "__main__":
    main()
