# Address Book

Core repository for adult contacts. Not for under 18s, who belong in Children (they can be moved either way after import: "How to move a contact to the Children module").

## Contact states

- **Active**: counts towards subscription, can be tagged, flowed, emailed, reported.
- **Pending**: awaiting consent or review (for example from forms). Not processed by flows or most reports.
- **Archived**: kept but inactive. Tags are unassigned on archive. Key dates "Left ministry" and "Left group" are added automatically when archiving people who were in ministries or small groups.
- **Deleted**: permanent. The person can no longer log in to My ChurchSuite or be seen. See "What happens when I archive / delete a contact or child" (articles 49 and 462) and 14-data-protection.md.

## Adding and managing contacts

- Contacts section, Add Contact. Standard fields, optional fields and custom fields.
- Merge duplicates: "Merging duplicate contacts and children" (article 359).
- Student details: Managing student details (article 30).
- Images: Managing images in ChurchSuite.
- Sex and gender: dedicated article (390) explains the fields and how they affect filters and smart tags.
- Households: Tracking household metrics (article 306). ChurchSuite links people at the same address across Address Book and Children.
- Bulk actions: Send email, Send SMS, Download CSV, Print labels/badges, batch edit (country, marital status, sex, site, communication options, My ChurchSuite and privacy settings). Article 499 covers batch actions.

## Tags

- **Fixed tags**: a list of people that only changes when a user changes it.
- **Smart tags**: a set of conditions, results update when underlying data changes and every night. Conditions can query fields like sex, age, postcode, other tags, key dates, custom fields, communication options, privacy settings, ministries, groups, flows and even Users and User Groups. Supports regular expressions. Recursion detection prevents loops.
- You can create a fixed tag from smart tag results ("Add to tag").
- Tags are admin only, not visible in My ChurchSuite.
- Warning: deleting a tag, key date, flow, group or ministry that a smart tag depends on breaks that smart tag.
- Empty tags are allowed (useful to prepare tags ahead).
- From a tag you can add the tagged people to a flow, group, key date or fixed tag, and view demographics.
- Sending email or SMS from a tag: use the bulk actions menu on the People tab.

## Key dates

Dated events against a person (First Visit, Baptism, Wedding, DBS check, Ongoing Consent, Right to be Forgotten). Used for pathway tracking, reminders and smart tag conditions. "Staying on top of member key dates" is article 31.

## Flows

Multi stage processes for moving people along (newcomer integration, membership, DBS renewal). Each stage has actions: add tag, add key date, add to group or ministry or team, send a preset email or SMS, and others. Overseers and users can be assigned to watch stages or actions and get emails when actions are due or overdue. Flows were redesigned in January 2022 (pop ups, faster with many people) and extend to Children, Giving givers and Bookings customers, with a choice of which modules share a flow (article 154).

## Custom fields

Add fields for anything not standard. Each custom field gets a merge field number derived from its internal ID, shown in Module Options. Custom fields can be made editable by contacts in My ChurchSuite or via a consent request. Article: "Custom fields for people".

## Forms

- Create forms with a Primary Response Type (Contacts or Children), publish and share (articles on Creating forms, Sharing published forms, Sending form invitations 730).
- Person detection: when a form is submitted ChurchSuite tries to match the response to an existing person. Auto-linking uses smart linked fields for First Name, Last Name, Email and Mobile (added 2025).
- Manage form responses in the module. The Data Protection checkbox helper text can be customised under Administrator, Profile.

## Consent and communication options

- Ongoing consent (article 474): My Consent requests let people update details and preferences; consent changes are logged and an "Ongoing Consent" key date is recorded.
- Communication options per person (email, SMS, etc.) with module defaults applied on creation and import.
- Preset emails and preset SMS: saved templates (articles 76 merge fields and the Presets articles).
- Communicating individually or to groups, tags and filters: see 12-communication-and-export.md.
- Notes and note visibility (article 44).
- Contact directory: Print labels/badges pop up can produce a printable Contact Directory (Address Book only), exported for collated printing or as PDF.

## Reports

Statistics report to track database changes over time (article 157), missing data reports, data cleaning reports, Demographics.

## Notes for admins

- Importing: see 13-import-and-migration.md. ChurchSuite never assumes people links between rows.
- Statuses and counts drive billing, so keep non-members out of Active unless you want to pay for them, or tag them and consider whether they should be Pending/Archived.
