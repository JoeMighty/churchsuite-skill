# /cs-import-check

Help prepare a CSV import.

1. Ask what is being imported: contacts, children or givers, and roughly how many rows.
2. Point to the template in assets/ and the checker in scripts/ (csv_preimport_check.py or giving_csv_check.py).
3. If the user pastes sample rows, review them by eye for: duplicate headers, header not in row 1, bad emails, bad dates, duplicate people, template example rows left in.
4. Warn: imported children are not linked to parents, always test a small batch, export existing data first.
5. Never ask the user to paste a full real list of personal data. Ask for a few anonymised rows.
