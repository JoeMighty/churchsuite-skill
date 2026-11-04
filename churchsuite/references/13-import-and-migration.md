# Import and migration

## Address Book import (article 11)

- File must be CSV, comma delimited, UTF-8. Row 1 holds column headers and each header must be unique, otherwise duplicate columns are ignored. The importer maps by header label.
- One person per row. ChurchSuite never assumes people links from different rows, so spouses and children are not linked automatically.
- One file can contain adults and children (for example John, Mary, Craig to Address Book and David, Maisey, Jack to Children), but then only basic child fields and Address Book custom fields can be mapped. Better: two files, imported separately into Address Book and Children.
- Review Address Book module settings first, because default communication options and My ChurchSuite and privacy settings are applied to everyone unless the CSV says otherwise.
- Review the field specifications list in the article and use the Missing Data reports afterwards.
- In a multi-site account, set the site on import.

## Children import (article 549)

Separate CSV imported into Children. Remove adult contacts, add them to the Address Book file. You can move records between modules after import. Link parents/carers afterwards with data cleaning reports.

## Giver import (article 292)

Import columns that ChurchSuite recognises. Unmatched headers show a yellow warning and are skipped. Includes Gift Aid declarations and spouse splits. After import use Potential Contacts to link givers to contacts.

## Donation import (article 51)

CSV or OFX bank statement. See 06-giving.md.

## Other imports

- Events import from CSV in Calendar.
- **Elvanto**: built in importer (article 642) copies data directly from the Elvanto database, no changes made to Elvanto. Choose communication defaults, then Start Import. Review Missing Data reports afterwards.
- From Planning Center, ChurchTrac and others: export CSV and use the Address Book importer. Reshape headers to match the importer's expected labels.

## Migration checklist

1. Export everything from the old system, including family and household IDs.
2. Split adults and children. Clean duplicates and statuses.
3. Decide on default consent, communication options and privacy before importing.
4. Import to a test or small batch first.
5. Verify counts, run Missing Data and Potential Contacts reports.
6. Link parents/carers and givers to contacts.
7. Rebuild tags, flows and key dates, then invite people to My ChurchSuite.
8. Keep the old system read only until the first month closes.
