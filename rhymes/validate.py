"""Check an agent's rhyme-pair TSV against the CMU dict and the brief.

usage: python validate.py CMUDICT GROUP PAIRS_TSV [--expect N] [--misses MISSES_TSV]

PAIRS_TSV columns (header row required):
  rank  word1  word2  rhyme_type  link  relationship  example

Every row must: use two qualifying words (in CMU, no r/l-controlled syllable),
have word1's stressed vowel in GROUP, carry the rhyme type CMU actually
supports, name a link from LINKS, give a 3-5 word relationship, and use both
words in the example. Ranks run 1..N. MISSES_TSV (columns: pair, reason)
must hold exactly five rows. Prints one line per problem; exit 1 if any.
"""

import csv
import re
import sys

from phonetics import GROUPS, base, load_cmu, qualifying, rhyme_type, stressed_index

ORDER = {"perfect": 0, "slant": 1, "assonance": 2}
LINKS = {"synonym", "antonym", "cause-effect", "part-whole", "scene"}
COLUMNS = ["rank", "word1", "word2", "rhyme_type", "link", "relationship", "example"]


def best_rhyme(q1, q2, group):
    """Strongest rhyme type, using word1 pronunciations stressed on GROUP."""
    found = None
    for pa in q1:
        if base(pa[stressed_index(pa)]) not in GROUPS[group]:
            continue
        for pb in q2:
            t = rhyme_type(pa, pb)
            if t and (found is None or ORDER[t] < ORDER[found]):
                found = t
    return found


def uses(example, word):
    return re.search(rf"\b{re.escape(word)}\b", example, re.IGNORECASE) is not None


def check(prons, group, rows):
    problems = []
    seen = set()
    for n, row in enumerate(rows, start=2):
        w1, w2 = row["word1"].strip().lower(), row["word2"].strip().lower()
        label = row["rhyme_type"].strip().lower()
        where = f"line {n} ({w1}/{w2})"

        if row["rank"].strip() != str(n - 1):
            problems.append(f"{where}: rank should be {n - 1}")
        if w1 == w2:
            problems.append(f"{where}: same word twice")
            continue
        key = tuple(sorted((w1, w2)))
        if key in seen:
            problems.append(f"{where}: duplicate pair")
        seen.add(key)

        q = {}
        for w in (w1, w2):
            if w not in prons:
                problems.append(f"{where}: '{w}' not in CMU dict")
                continue
            q[w] = qualifying(prons[w])
            if not q[w]:
                problems.append(f"{where}: '{w}' has an r- or l-controlled syllable")
        if len(q) < 2 or not q[w1] or not q[w2]:
            continue

        vowels = {base(p[stressed_index(p)]) for p in q[w1]}
        if not vowels & GROUPS[group]:
            problems.append(f"{where}: '{w1}' stressed vowel {sorted(vowels)} "
                            f"is not in {group} {sorted(GROUPS[group])}")
            continue

        actual = best_rhyme(q[w1], q[w2], group)
        if actual is None:
            problems.append(f"{where}: no perfect/slant/assonance link in CMU")
        elif label != actual:
            problems.append(f"{where}: labelled '{label}' but CMU gives '{actual}'")

        if row["link"].strip().lower() not in LINKS:
            problems.append(f"{where}: link must be one of {sorted(LINKS)}")
        words = len(row["relationship"].split())
        if not 3 <= words <= 5:
            problems.append(f"{where}: relationship must be 3-5 words, got {words}")
        for w in (w1, w2):
            if not uses(row["example"], w):
                problems.append(f"{where}: example does not use '{w}'")
    return problems


def read_tsv(path):
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
        return reader.fieldnames or [], list(reader)


def check_misses(rows):
    problems = []
    if len(rows) != 5:
        problems.append(f"near-misses: expected 5 rows, found {len(rows)}")
    for n, r in enumerate(rows, start=2):
        if not (r.get("pair") or "").strip() or not (r.get("reason") or "").strip():
            problems.append(f"near-misses line {n}: needs a pair and a reason")
    return problems


def main():
    args = sys.argv[1:]
    opts = {}
    for flag in ("--expect", "--misses"):
        if flag in args:
            i = args.index(flag)
            opts[flag] = args[i + 1]
            del args[i:i + 2]
    cmu_path, group, pairs_path = args
    if group not in GROUPS:
        sys.exit(f"unknown group {group}; choose from {', '.join(GROUPS)}")

    fields, rows = read_tsv(pairs_path)
    missing = [c for c in COLUMNS if c not in fields]
    if missing:
        sys.exit(f"missing columns: {', '.join(missing)}")

    problems = check(load_cmu(cmu_path), group, rows)
    if "--expect" in opts and len(rows) != int(opts["--expect"]):
        problems.append(f"expected {opts['--expect']} rows, found {len(rows)}")
    if "--misses" in opts:
        problems += check_misses(read_tsv(opts["--misses"])[1])
    for p in problems:
        print(p)
    print(f"{len(rows)} rows, {len(problems)} problems")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
