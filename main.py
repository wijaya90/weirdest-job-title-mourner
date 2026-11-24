#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown entry.

Writes one job title to /output/entry.txt: a professional mourner hired
to grieve at the funerals of complete strangers. A real odd job
(professional mourning exists) with one hilariously specific twist — the
dead are strangers, so the grief is strictly professional.
"""
import os
import sys

TITLE = "Professional Mourner for Funerals of Complete Strangers"

def main():
    # Gate: UTF-8 text of 1 to 60 characters, not only white space.
    if not TITLE.strip() or len(TITLE) > 60 or "\n" in TITLE:
        print(f"entry violates gate: {len(TITLE)} chars", file=sys.stderr)
        raise SystemExit(1)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TITLE)

if __name__ == "__main__":
    main()
