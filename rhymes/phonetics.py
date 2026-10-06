"""Shared CMU-dict helpers for the rhyme-pair project.

Rules enforced here (from the brief):
  * exactly two syllables in every CMU pronunciation, stress pattern iamb
    (0-1 / 2-1) or trochee (1-0 / 1-2)
  * no r-controlled syllables: no ER vowel, and no vowel immediately followed by R
  * no l-controlled syllables: no vowel immediately followed by L, except a long
    vowel in an open syllable whose L starts the next syllable (ho-ly, si-lent),
    and no silent-L spelling (talk, calm) or suffixed base-final L (roll-ing)
"""

import re

VOWELS = {"AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY",
          "IH", "IY", "OW", "OY", "UH", "UW"}
LONG = {"EY", "IY", "AY", "OW", "UW", "AW", "OY"}

# One agent per vowel. Long U includes the "yoo" glide (music, beauty);
# short O includes AO, which phonics also teaches as short o (dog, cloth).
GROUPS = {
    "long_a": {"EY"},
    "long_e": {"IY"},
    "long_i": {"AY"},
    "long_o": {"OW"},
    "long_u": {"UW"},
    "short_a": {"AE"},
    "short_e": {"EH"},
    "short_i": {"IH"},
    "short_o": {"AA", "AO"},
    "short_u": {"AH"},
}

# Consonant pairs close enough to count as a slant (voicing / place neighbours).
NEAR = [{"P", "B"}, {"T", "D"}, {"K", "G"}, {"F", "V"}, {"S", "Z"},
        {"TH", "DH"}, {"SH", "ZH"}, {"CH", "JH"}, {"M", "N"}, {"N", "NG"},
        {"M", "NG"}, {"S", "SH"}, {"Z", "ZH"}, {"T", "K"}, {"D", "G"},
        {"P", "T"}, {"B", "D"}, {"F", "TH"}, {"V", "DH"}]

WORD_RE = re.compile(r"^[a-z]+$")
SILENT_L = re.compile(r"alk|alm|alf|alv|olk|ould")
# A base word that ends in vowel + L keeps that L in its own syllable when a
# suffix is added (roll-ing, feel-ing, smil-ing, styl-ish).
BASE_FINAL_L = re.compile(r"[aeiouwy]ll?(ing|ings|ish)$")


def load_cmu(path):
    """Return {word: [phoneme lists]} for plain alphabetic entries."""
    prons = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.split("#", 1)[0].strip()
            if not line:
                continue
            head, *phones = line.split()
            word = re.sub(r"\(\d+\)$", "", head)
            if WORD_RE.match(word):
                prons.setdefault(word, []).append(phones)
    return prons


def base(ph):
    return ph.rstrip("012")


def is_vowel(ph):
    return base(ph) in VOWELS


def meter(phones):
    """'iamb', 'trochee', or None."""
    stresses = [ph[-1] for ph in phones if is_vowel(ph)]
    if len(stresses) != 2:
        return None
    pattern = "".join(stresses)
    if pattern in ("01", "21"):
        return "iamb"
    if pattern in ("10", "12"):
        return "trochee"
    return None


def controlled(phones):
    """True if any syllable is r- or l-controlled.

    An L/R right after a vowel controls it when it closes that vowel's
    syllable: before a consonant or word end (ball, morning), or between
    vowels after a stressed short vowel (jelly, carry). After an unstressed
    vowel it starts the next syllable instead (de-light, a-rise). A stressed
    long vowel stays open before L (ho-ly, si-lent) but is r-coloured before
    R in American English (he-ro, si-ren), so that still counts. CMU writes
    a schwa before an R-onset as ER0 (a-rise, pa-rade); that R starts the
    next syllable, so it is allowed too.
    """
    for i, ph in enumerate(phones):
        if not is_vowel(ph):
            continue
        v = base(ph)
        nxt = phones[i + 1] if i + 1 < len(phones) else None
        if v == "ER":
            if ph == "ER0" and nxt is not None and is_vowel(nxt):
                continue
            return True
        if nxt not in ("L", "R"):
            continue
        after = phones[i + 2] if i + 2 < len(phones) else None
        if after is None or not is_vowel(after):
            return True
        if ph.endswith("0"):
            continue
        if v not in LONG or nxt == "R":
            return True
    return False


def stressed_index(phones):
    for i, ph in enumerate(phones):
        if is_vowel(ph) and ph.endswith("1"):
            return i
    return None


def norm(ph):
    """Strip stress; fold reduced unstressed vowels together (schwa)."""
    if is_vowel(ph):
        if ph[-1] == "0" and base(ph) in {"AH", "IH", "EH", "UH"}:
            return "@"
        return base(ph)
    return ph


def vowelish(sym):
    """True for a normalised vowel symbol (including the folded schwa)."""
    return sym == "@" or sym in VOWELS


def tail(phones):
    i = stressed_index(phones)
    return [norm(p) for p in phones[i:]]


def onset(phones):
    i = stressed_index(phones)
    return [norm(p) for p in phones[:i]]


def is_near(a, b):
    return a == b or {a, b} in NEAR


def rhyme_type(p1, p2):
    """Classify the sound link between two pronunciations.

    perfect   - identical from the stressed vowel to the end, different onset
    slant     - same stressed vowel with near consonants (<=2 near swaps), or
                a different stressed vowel over identical following sounds
    assonance - same stressed vowel, other sounds differ
    None      - no qualifying sound link
    """
    t1, t2 = tail(p1), tail(p2)
    if t1 == t2:
        return "perfect" if onset(p1) != onset(p2) else None
    if t1[0] == t2[0]:
        if len(t1) == len(t2):
            diffs = [(a, b) for a, b in zip(t1, t2) if a != b]
            if len(diffs) <= 2 and all(not vowelish(a) and not vowelish(b) and is_near(a, b)
                                       for a, b in diffs):
                return "slant"
        return "assonance"
    if t1[1:] == t2[1:] and len(t1) > 1:
        return "slant"
    return None


def qualifying(prons, word=None):
    """Pronunciations of a word that satisfy the brief's sound rules.

    A word whose CMU entries disagree on syllable count (cov-ring vs
    co-ver-ing, gig-gling vs gig-gle-ing) is dropped: its meter is ambiguous.
    Given the spelling, so is a silent-L pattern (talk, calm, half, folk,
    could), which phonics teaches as l-controlled though CMU has no L, and a
    suffixed base-final L (rolling, feeling, smiling), whose L stays with the
    stressed vowel even though CMU writes it before the suffix's vowel.
    """
    if word is not None and (SILENT_L.search(word) or BASE_FINAL_L.search(word)):
        return []
    if any(sum(is_vowel(ph) for ph in p) != 2 for p in prons):
        return []
    out = []
    for p in prons:
        m = meter(p)
        if m and not controlled(p):
            out.append((m, p))
    return out
