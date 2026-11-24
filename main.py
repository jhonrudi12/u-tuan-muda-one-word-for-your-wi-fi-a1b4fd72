#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun bounty entry.

Writes a single word to /output/entry.txt: the funniest, truest
one-word description of home Wi-Fi, chosen by scoring a shortlist
against the judge's brief (on-subject first, then funny, then true,
then fresh, then instantly readable with no context needed).
"""

import os

# Candidates, scored 0-5 on the judge's criteria in order:
# (on-subject, funny at once, true to home Wi-Fi, fresh angle, readable)
CANDIDATES = {
    "Ghosting":   (5, 4, 5, 4, 5),
    "Gaslighting": (5, 5, 5, 5, 5),
    "Flaky":      (5, 3, 5, 2, 5),
    "Moody":      (5, 3, 4, 3, 5),
    "Diva":       (4, 4, 3, 4, 5),
    "Liar":       (5, 3, 4, 3, 5),
    "Catfish":    (4, 4, 3, 4, 4),
    "Buffering":  (5, 2, 5, 1, 5),
}

# Judge weighs the criteria most important first, so earlier
# criteria count more than later ones.
WEIGHTS = (5, 4, 3, 2, 1)


def score(word: str) -> int:
    """Weighted score of one candidate word."""
    return sum(w * s for w, s in zip(WEIGHTS, CANDIDATES[word]))


def pick_word() -> str:
    """Return the highest-scoring word; ties break to the shorter word."""
    return min(CANDIDATES, key=lambda w: (-score(w), len(w)))


def main() -> None:
    word = pick_word()
    assert 1 <= len(word) <= 20, "entry must be 1-20 characters"
    assert word.strip(), "entry must not be only whitespace"
    assert " " not in word, "entry must be a single word"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)
    print(word)


if __name__ == "__main__":
    main()
