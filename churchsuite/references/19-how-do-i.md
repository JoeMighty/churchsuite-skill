# How do I...? Task playbooks

Plain English, task first. Each playbook gives where to go, the steps, and what commonly goes wrong. Menu names can shift as ChurchSuite updates, so if a button is not where described, search the matching article in 18-source-index.md. Before any bulk or destructive step, export a CSV first.

Last verified against public support content: November 2026.

## People

**1. Add a new person**
Address Book, Add contact (adults) or Children module, Add child. Fill name and at least one contact method. Set status Active so they appear in flows, tags and emails. Watch out: Pending and Archived contacts are skipped by automation.

**2. Find a person quickly**
Use the search box at the top of the module. Search by name, email or phone. For groups of people use a tag (see 9) rather than searching repeatedly.

**3. Edit many people at once**
Address Book, People tab, tick people, use the bulk actions menu. Export a CSV first. Bulk changes are hard to reverse.

**4. Link a child to parents or carers**
Open the child, add the parent or carer relationship. Imports do not link them, so do it manually or fix it from the data cleaning reports.

**5. Merge duplicate people**
Use Merge duplicate contacts (and the equivalent for children). Review the pair, choose which values to keep. Merge is permanent. Check person detection settings on forms to stop new duplicates.

**6. Archive or delete someone**
Archive to keep history and stop processing. Delete only when you have no lawful reason to keep data. Delete is permanent. See 14-data-protection.md.

**7. Record a key date (baptism, membership, DBS check)**
Open the person, Key dates, add a date, or add the key date in bulk from the People tab. Key dates can drive reports, smart tags and flows.

## Organising people

**8. Make a list of people (fixed tag)**
Create a tag, add people by hand. Use for curated lists such as a prayer team.

**9. Make a list that updates itself (smart tag)**
Create a smart tag with conditions (for example: Active, has key date X, in group Y). Membership follows the data. Do not delete tags, key dates, flows or groups that a smart tag depends on, or the conditions break.

**10. Follow up newcomers automatically (flow)**
Create a flow with stages and tasks, then add people from a form or by hand. Only Active contacts are processed. Use the My Details newcomer form to feed it.

**11. Use custom fields**
Add them in the module settings, then place them on forms and views. Keep names plain and consistent (see assets/naming-conventions.md).

## Communicating

**12. Email a group**
People tab, tick people or open a tag, bulk actions, Send email. (The Send email button moved to the bulk actions menu in 2025.) Preview before sending. Check communication options.

**13. Send an SMS**
Same bulk actions menu, SMS, if SMS credits are set up under Account Settings. Keep texts short and include who it is from.

**14. Use merge fields**
Insert fields such as the first name from the editor. Some only work in one context, for example `::my_link::` in invitation emails and `::roles::` and `::serving_date::` in rota reminders. Use scripts/merge_field_lint.py to catch typos.

**15. Fix an email that bounced**
Check Email errors in the module, confirm the address, and check sender domain authentication if using a shared address.

**16. Export a mailing or label list**
Use CSV export or label printing from the People tab. See 12-communication-and-export.md.

## Getting data in and out

**17. Import people from a spreadsheet**
Use the import template in assets/import-contacts.csv. Header in row 1, no duplicate headers. Run scripts/csv_preimport_check.py first. Imported children are not linked to parents. Import into a test tag or a small batch first.

**18. Import givers**
Use assets/import-givers.csv and scripts/giving_csv_check.py. A yellow triangle on a column means the label was not recognised.

**19. Migrate from another system**
Read 13-import-and-migration.md. Export everything, clean in a spreadsheet, import in stages (contacts, then children, then givers), spot check.

**20. Export data for backup**
Export CSVs from each module on a schedule, store them securely, and delete old copies you no longer need.

## Calendar and events

**21. Add an event**
Calendar, Add event. Set date, time, site, and whether it shows in My ChurchSuite or in embeds ("Show in embed"). Recurring events are sequences.

**22. Change one occurrence or the whole series**
Edit and choose whether the change applies to the sequence. This is the most common surprise, so check the prompt.

**23. Let people sign up to an event**
Add a sign up form or tickets on the event. Registrations can create or match contacts via person detection.

**24. Put events on the website**
Create an Embed configuration (Calendar, Embed tab), paste the generated HTML or use the JSON feed. See 15-developer-api-and-embed.md.

## Children and Check-In

**25. Set up Sunday check-in**
Create sessions and groups in Children, set up the Check-In app on each device, run a Print test, and brief volunteers. Use assets/sunday-checkin-checklist.md. The old Connect child check-in was retired on 31 May 2026.

**26. Fix a child missing at check-in**
Check they are in the group member list, the age group fits, and the parent has a QR code through My ChurchSuite.

**27. Record allergies and consent**
Use the child's record fields and consents. Treat as sensitive data. Restrict who can view.

## Small groups

**28. Create a group and add members**
Small Groups, Add group, set leaders, meeting day and site. Add members by hand or via sign up. Use labels and clusters to organise.

**29. Take group attendance**
Leaders record attendance in My ChurchSuite or the admin side. See 04-small-groups.md.

## Rotas

**30. Build a rota**
Rotas, create ministry, teams and roles, add a rota, assign it to services, add people, send. See 05-rotas.md.

**31. Handle a swap or a gap**
Members organise a swap in My Rotas. If it clashes, an overseer or module user processes it. Unavailability blocks all rotas, decline blocks one date.

**32. Turn on unavailability**
Module Options, Unavailability, Edit.

## Giving

**33. Record a donation**
Giving, Add donation against a giver and fund, or import a bank file. Only credits import from bank files.

**34. Set up Gift Aid**
Add a declaration for the giver with correct dates. Claim from Gift Aid claims. Donate declarations are fund specific. See 06-giving.md. This is UK specific.

**35. Fix an unclaimable donation**
Correct the declaration dates or scope. Donations return to Unclaimed and can go in the next claim.

## Bookings and rooms

**36. Book a room**
Bookings, Add booking, choose resources and dates. Watch clashes. A booking with a paid online charge cannot be deleted.

## Account and admin

**37. Add a user and set permissions**
Account Settings, Users. Set Administrator or User, then None, Use, Write or Manage per module, plus site access. Give the least needed. See assets/permission-matrix.md.

**38. Turn on My ChurchSuite for members**
Module My ChurchSuite Options tabs control what members see. Send invitations with `::my_link::`.

**39. Handle a data request**
Subject access: export what you hold for that person. Right to be forgotten: ChurchSuite notifies the data protection contact and adds a key date, nothing is auto deleted. You decide. See 14-data-protection.md.

**40. Set up API access**
Administrator enables API access for a dedicated user, the user creates the secret. Use read only scopes. See 15-developer-api-and-embed.md and scripts/churchsuite_client.py.
