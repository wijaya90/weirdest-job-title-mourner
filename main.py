#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown entry.

Writes one job title to /output/entry.txt: a professional mourner hired
to grieve at the funerals of complete strangers. A real odd job
(professional mourning exists) with one hilariously specific twist — the
dead are strangers, so the grief is strictly professional.
"""
import os

TITLE = "Professional Mourner for Funerals of Complete Strangers"

def validate(title):
    """Check the 1-60 char single-line contract.

    Returns the title unchanged when it passes; raises SystemExit
    with a diagnostic otherwise, so a bad title can never reach
    the output file.
    """
    if not isinstance(title, str):
        raise SystemExit("entry must be text")
    if not title.strip():
        raise SystemExit("entry must not be blank")
    if len(title) > 60:
        raise SystemExit(f"entry too long: {len(title)} chars (max 60)")
    if "\n" in title or "\r" in title:
        raise SystemExit("entry must be a single line")
    return title

def main():
    title = validate(TITLE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(title)

if __name__ == "__main__":
    main()
