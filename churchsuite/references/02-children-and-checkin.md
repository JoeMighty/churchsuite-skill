# Children module and Check-In

## Children module

Manages children and young people (typically under 18), their parents/carers and age based groups. Has its own address book layout like the Address Book.

### Key concepts

- **Group Setup**: container for one or more age based **Groups**. Groups have age entry criteria, a maximum age for the Group Setup, optional room capacity.
- **Gatherings**: attendance headings for children's meetings (Adding and managing gatherings).
- **Parents/carers**: linked Address Book contacts. A primary parent/carer can manage children's details in My ChurchSuite. ChurchSuite never auto links parents during import: link afterwards using the data cleaning reports (Linking children with parents/carers).
- **Visitors**: visiting children who are not in the database, managed under Managing details of visiting children. A visitor retention setting removes visitors who have not checked in beyond the retention period.
- **Consent**: Ongoing consent, internal and external photo/video consent (smart tag conditions exist for both), privacy settings.
- **Age of consent for My ChurchSuite**: set in Children module settings. Children below it, or without a date of birth, cannot be invited or log in. Age is verified at each login.

### Processing children into new groups as they age

Each group has a Process feature. It compares each child's age (from date of birth) with the age criteria of all Groups in the Group Setup. One click processes a whole group. Use Change date to process for a future date (for example the start of the school year). Children past the Group Setup maximum age and not eligible for any other group can be processed out. Saving applies immediately even if a future date is chosen.

### Other topics

- Importing: dedicated CSV import (article 549). Only basic child fields are available via the Address Book importer.
- Moving children to the Address Book and vice versa.
- Custom fields, flows, key dates, smart and fixed tags, notes, forms (same patterns as Address Book).
- Running holiday clubs, managing parent and toddler groups (case style articles).
- Birthdays in ChurchSuite.
- Reporting: child attendance reporting (article 327), Sessions report (moved to Attendance, Sessions section), custom reports and CSV export, statistics report.
- Add to tag, key date or flow from the group attendance view.

## Check-In system

Modern standalone Check-In app (iOS App Store, Android Play Store, and in a browser at login). It replaced Connect child check-in, which was retired on 31 May 2026. Same sessions, templates and groups carry over, with no change in Children module functionality. Articles: 682 Getting started, 651 Running a session, 694 Session templates, 684 Connecting a printer, 392 Child check-in operation.

### Modes

- **Register and Check-in (one stage)**: children go straight to groups. Attendance is added to the Children module as each child is checked in.
- **Register first, Check in later**: children stay with parents/carers at first. Leaders check them into groups from the group page in the Admin area when handed over.
- Configurations: central **Register** point, **in-room** by leaders, or unstaffed **Kiosk** for parents/carers.

### Features

- Session templates to start sessions quickly.
- Check-In user permissions control who can start, use, edit and close sessions. Device settings (such as showing/hiding empty groups, Group lock to check all children into one group regardless of age) are remembered per device.
- Check in adults as attendees or team members.
- QR codes: parents/carers with My ChurchSuite access get a Check-In QR code in My Children while a session is active. Scanning at the station lists all linked children. Parent pick up passes appear after check in.
- Room capacity enforcement prevents further check ins once reached.
- Badges and printing: compatible **Brother** label printers. Bluetooth printers must be re-paired after power cycling unless the Brother Printer Settings Tool auto reconnect is enabled. USB: recommended Windows with Google Chrome for silent printing in kiosk mode. Admin menu has Print test for child, attendee and team badges, so test each device at the start of each session. Silent browser printing has its own article. Wireless Brother set up from Mac is documented in the Connect app article (472).
- Manual fallback: print registers and badges from the Group Setup (Print register, Print badges), tick children present, then record attendance manually (article 166). Register can filter by tags and include Medical Short data, ordered by first or last name.
- Multi-site and Check-In interplay is covered in the multi-site article (216).

### Connect (information point tools)

Connect runs on a device at the information desk: newcomer form (My Details) and edit mode for members, Donate (browser only, not in the Android Connect app), small group sign-up, event sign-up. Android Connect app is on the Play Store (separate from the ChurchSuite admin/member app). iOS users use Safari.

## Gotchas

- Silent printing needs Chrome on Windows in kiosk mode.
- Children without a date of birth cannot be age processed or invited to My ChurchSuite.
- Imported children are not linked to parents automatically.
- Legacy Connect check-in is retired. Point people to the Check-In app.
