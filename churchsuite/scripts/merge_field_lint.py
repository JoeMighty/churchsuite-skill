#!/usr/bin/env python3
"""Lint ChurchSuite merge fields in a text file. Stdlib only, read only.

Usage: python3 merge_field_lint.py draft.txt
Flags: unclosed ::fields::, spaces inside fields, uppercase fields, and fields that
only work in certain contexts. The known field list is deliberately short: check your
account's editor for the full list and add names to KNOWN below.
"""
import re
import sys

KNOWN = {"first_name", "last_name", "name", "my_link", "roles", "serving_date"}
CONTEXT = {
    "my_link": "only works in My ChurchSuite invitation emails",
    "roles": "only works in rota reminders",
    "serving_date": "only works in rota reminders",
}


def main(path):
    text = open(path, encoding="utf-8").read()
    problems = []
    if text.count("::") % 2:
        problems.append("Odd number of '::' so a field is probably unclosed")
    for m in re.finditer(r"::([^:\n]*)::", text):
        name = m.group(1)
        if name != name.strip() or " " in name:
            problems.append(f"Spaces inside field '::{name}::'")
        elif name != name.lower():
            problems.append(f"Field '::{name}::' should be lowercase")
        elif name not in KNOWN:
            problems.append(f"Unknown field '::{name}::' (check the editor, or add to KNOWN)")
        elif name in CONTEXT:
            problems.append(f"Note: '::{name}::' {CONTEXT[name]}")
    if problems:
        for p in problems:
            print(" -", p)
        return 1
    print("No problems found.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
