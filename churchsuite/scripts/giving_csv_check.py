#!/usr/bin/env python3
"""Check a giving CSV before import. Stdlib only, read only.

Usage: python3 giving_csv_check.py donations.csv
Looks for missing amounts, negative amounts, bad dates, future dates, missing funds,
and duplicate rows. Never modifies the file.
"""
import csv
import sys
from collections import Counter
from datetime import date, datetime


def parse_date(v):
    for fmt in ("%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(v, fmt).date()
        except ValueError:
            pass
    return None


def main(path):
    problems = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        cols = {c.lower().strip(): c for c in (reader.fieldnames or [])}
        for need in ("amount", "date", "fund"):
            if need not in cols:
                problems.append(f"Missing column: {need}")
        seen = Counter()
        for i, row in enumerate(reader, start=2):
            key = tuple(v.strip() for v in row.values())
            seen[key] += 1
            amt = row.get(cols.get("amount", ""), "").strip()
            try:
                if float(amt) <= 0:
                    problems.append(f"Row {i}: amount must be positive ({amt})")
            except ValueError:
                problems.append(f"Row {i}: amount not a number ('{amt}')")
            d = parse_date(row.get(cols.get("date", ""), "").strip())
            if d is None:
                problems.append(f"Row {i}: date not YYYY-MM-DD or D/M/YYYY")
            elif d > date.today():
                problems.append(f"Row {i}: date is in the future")
            if not row.get(cols.get("fund", ""), "").strip():
                problems.append(f"Row {i}: fund is empty")
        for key, n in seen.items():
            if n > 1:
                problems.append(f"Identical row appears {n} times: {key}")
    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print(" -", p)
        return 1
    print("No problems found. Compare the total with your bank statement.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
