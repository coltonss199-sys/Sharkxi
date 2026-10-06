"""Check an agent's rhyme-pair TSV against the CMU dict and the brief.

usage: python validate.py CMUDICT GROUP PAIRS_TSV [--expect N]

PAIRS_TSV columns (header row required):
  rank  word1  meter1  word2  meter2  rhyme_type  relationship  example

Every row must: use two qualifying words (2 syllables, labelled meter matches
CMU, no r/l-controlled syllable), have word1's stressed vowel in GROUP, carry
the rhyme type CMU actually supports, give a 3-5 word relationship, and use
both words in the example. Prints one line per problem; exit status 1 if any.
"""

import csv
import sys

from phonetics import GROUPS, base, load_cmu, qualifying, rhyme_type, stressed_index

ORDER = {"perfect": 0, "slant": 1, "assonance": 2}
COLUMNS = ["rank", "word1", "meter1", "word2", "meter2",
           "rhyme_type", "relationship", "example"]


def best_rhyme(q1, q2, m1, m2):
    """Strongest rhyme type over pronunciations matching the labelled meters."""
    found = None
    for ma, pa in q1:
        for mb, pb in q2:
            if ma != m1 or mb != m2:
                continue
            t = rhyme_type(pa, pb)
            if t and (found is None or ORDER[t] < ORDER[found]):
                found = t
    return found


def check(prons, group, rows):
    problems = []
    seen = set()
    for n, row in enumerate(rows, start=2):
        w1, w2 = row["word1"].strip().lower(), row["word2"].strip().lower()
        m1, m2 = row["meter1"].strip().lower(), row["meter2"].strip().lower()
        label = row["rhyme_type"].strip().lower()
        where = f"line {n} ({w1}/{w2})"

        if w1 == w2:
            problems.append(f"{where}: same word twice")
            continue
        key = tuple(sorted((w1, w2)))
        if key in seen:
            problems.append(f"{where}: duplicate pair")
        seen.add(key)

        q = {}
        for w, m in ((w1, m1), (w2, m2)):
            if w not in prons:
                problems.append(f"{where}: '{w}' not in CMU dict")
                continue
            q[w] = qualifying(prons[w], w)
            if not q[w]:
                problems.append(f"{where}: '{w}' breaks the rules "
                                "(not 2-syllable iamb/trochee, or r/l-controlled)")
            elif m not in {mm for mm, _ in q[w]}:
                problems.append(f"{where}: '{w}' is not a {m}; CMU says "
                                f"{sorted({mm for mm, _ in q[w]})}")
        if len(q) < 2 or not q[w1] or not q[w2]:
            continue

        vowels = {base(p[stressed_index(p)]) for mm, p in q[w1] if mm == m1}
        if not vowels & GROUPS[group]:
            problems.append(f"{where}: '{w1}' stressed vowel {sorted(vowels)} "
                            f"is not in {group} {sorted(GROUPS[group])}")

        actual = best_rhyme(q[w1], q[w2], m1, m2)
        if actual is None:
            problems.append(f"{where}: no perfect/slant/assonance link in CMU")
        elif label != actual:
            problems.append(f"{where}: labelled '{label}' but CMU gives '{actual}'")

        words = len(row["relationship"].split())
        if not 3 <= words <= 5:
            problems.append(f"{where}: relationship must be 3-5 words, got {words}")

        example = row["example"].lower()
        for w in (w1, w2):
            if w not in example:
                problems.append(f"{where}: example does not use '{w}'")
    return problems


def main():
    args = sys.argv[1:]
    expect = None
    if "--expect" in args:
        i = args.index("--expect")
        expect = int(args[i + 1])
        del args[i:i + 2]
    cmu_path, group, pairs_path = args
    if group not in GROUPS:
        sys.exit(f"unknown group {group}; choose from {', '.join(GROUPS)}")

    with open(pairs_path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        missing = [c for c in COLUMNS if c not in (reader.fieldnames or [])]
        if missing:
            sys.exit(f"missing columns: {', '.join(missing)}")
        rows = list(reader)

    problems = check(load_cmu(cmu_path), group, rows)
    if expect is not None and len(rows) != expect:
        problems.append(f"expected {expect} rows, found {len(rows)}")
    for p in problems:
        print(p)
    print(f"{len(rows)} rows, {len(problems)} problems")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
