#!/usr/bin/env python3
"""Check a people CSV before importing into ChurchSuite. Stdlib only, read only.

Usage: python3 csv_preimport_check.py people.csv
Reports: header problems, duplicate headers, bad emails, bad dates, duplicate emails,
empty rows. Never modifies the file.
"""
import csv
import re
import sys
from collections import Counter

EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
DATE = re.compile(r"^(\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{4})$")


def main(path):
    problems = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    if not rows:
        print("File is empty")
        return 1
    header = [h.strip() for h in rows[0]]
    dup = [h for h, n in Counter(header).items() if n > 1 and h]
    if dup:
        problems.append(f"Duplicate headers (ChurchSuite ignores these): {dup}")
    if any(not h for h in header):
        problems.append("Blank header cell(s) in row 1")
    low = [h.lower() for h in header]
    emails = Counter()
    for i, row in enumerate(rows[1:], start=2):
        if not any(c.strip() for c in row):
            problems.append(f"Row {i}: empty row")
            continue
        if len(row) != len(header):
            problems.append(f"Row {i}: {len(row)} cells but header has {len(header)}")
        for col, val in zip(low, row):
            val = val.strip()
            if not val:
                continue
            if "email" in col and not EMAIL.match(val):
                problems.append(f"Row {i}: invalid email '{val}'")
            if "email" in col:
                emails[val.lower()] += 1
            if ("date" in col or "birth" in col) and not DATE.match(val):
                problems.append(f"Row {i}: date '{val}' not YYYY-MM-DD or D/M/YYYY")
            if val.lower().startswith("example row"):
                problems.append(f"Row {i}: template example row still present")
    for e, n in emails.items():
        if n > 1:
            problems.append(f"Email used {n} times (possible duplicate people): {e}")
    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print(" -", p)
        return 1
    print("No problems found. Still import a small test batch first.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
