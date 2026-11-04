# Communication, labels and export

Support category: Communication (21 articles).

## Email and SMS

- Available in people modules (Address Book, Children, Giving, Bookings customers, Small Groups, Network, Calendar sign ups, Rotas).
- Choose recipients: All, individuals, by tag, by group/cluster/ministry, or filtered contact lists. Since 2025 filters and bulk actions changed: Contacts page has Compose new email (no recipients selected) and Send email from filtered lists, and Send email/SMS inside a tag sits in the People tab bulk actions menu.
- Child communications go to parents/carers, with older children optionally copied.
- Branded emails with brands, signatures and preset content. Email deliverability monitoring and email errors list. Scheduled SMS. Provider integrations: BulkSMS, Twilio, Textlocal. Shared from addresses must be authenticated (see Sending emails from a shared email address).
- The communications log records every email and SMS sent. Members see theirs in My Communication.
- Preset emails and SMS keep standard content. Take care saving an email with merge fields as a preset, because some merge fields only work in certain contexts.

## Merge fields (article 76)

Syntax is `::field_name::`. Not all fields work in both email and SMS or in every context.

| Merge field | Meaning |
|---|---|
| `::first_name::`, `::last_name::`, `::contact_name::` | Recipient name |
| `::email::`, `::mobile::`, `::cellular::` | Recipient contact details |
| `::contact_details::` | Address, telephone, mobile, email block (email, and limited use in SMS) |
| `::full_address::` | Recipient address (obscured in the example) |
| `::my_link::`, `::my_registration_link::` | My ChurchSuite login and registration URLs. Only in invitation and details reminder emails. Email only |
| `::roles::`, `::serving_date::` | Only in rota reminders (email and SMS) |
| custom field merge fields | Numbered from internal field ID, shown in Module Options next to each custom field |

Merge fields relate to the recipient, which may differ from the subject person (for example a parent receiving a child email).

## Labels and badges

Print labels/badges pop up produces address labels, name badges and (Address Book) a contact directory. The last used label format persists per device.

## CSV export (article 419, 43)

- Each module has a primary section: Address Book Contacts, Children Children (and Visitors), Calendar Events, Small Groups Groups, Giving Givers, Bookings Customers, Network Organisations.
- Choose columns or presets, filter, then Bulk actions: Send email, Send SMS, Download CSV, Print labels/badges. Bulk actions respect filters and show the number selected. On screen tables are paginated, but CSV and print include all matching records.
- Export options include internal Contact ID, Spouse ID, Child ID and Parent ID, enough to cross match families when migrating.
- Bulk actions also edit data in bulk.

## Mail merge to Word (article 71)

Module Communication page, choose recipients (All, Individual, By Tag), optionally filter (sex, parents, custom fields), CSV Options, switch from Custom Selection to Mail Merge, optionally include children's first names, Export to CSV, then use Word's mail merge. For labels, prefer printing labels directly in ChurchSuite.
