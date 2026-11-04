# Troubleshooting and gotchas

## People and data

| Symptom | Likely cause and fix |
|---|---|
| Person missing from a flow, tag or email | They are Pending or Archived. Only Active contacts are processed. Move to Active. |
| Smart tag shows odd results after a cleanup | A dependent tag, key date, flow, group or ministry was deleted, which breaks conditions. Re-edit the smart tag. |
| Smart tag results stale | They refresh when data changes and nightly. Wait or edit a dependent data point. |
| Imported columns ignored | Duplicate header labels, header not in row 1, or label not recognised (yellow triangle on givers import). |
| Imported children not linked to parents | By design. Link manually and use data cleaning reports. |
| Duplicate people | Use Merge duplicate contacts and children. Check person detection settings on forms. |
| Child cannot log in to My ChurchSuite | Below Age of Consent, no date of birth, or Allow login not ticked. |
| Cannot add a person to a site | User lacks All sites or that site permission. |
| "Forget me" button not shown | No Data Protection statement uploaded in Profile, or US account. |

## Communication

| Symptom | Fix |
|---|---|
| Merge field blank | Field only works in a specific context (`::my_link::` only in invitation emails, `::roles::` and `::serving_date::` only in rota reminders). |
| Email bounced or not received | Check Email errors, sender domain authentication for shared addresses, communication options for the person. |
| Child email goes to parent | Child communications go to parents/carers by default. |
| Where did the Send email button go in a tag | It moved to the bulk actions menu on the People tab (2025). |

## Rotas

- Cannot process a swap: swap would clash for the other person, ask an overseer or module user.
- Unavailability for the coming Sunday: arrange a swap instead.
- Overlapping rotas showing false clashes: disable clash detection on those rotas.
- iCal rota feed not updating: refreshes every 24 hours. Android cannot subscribe natively.

## Check-In

- Badge will not print silently: use Windows with Chrome in kiosk mode, or Bluetooth printer re-paired. Run Print test on each device each session.
- Child not listed at check in: not in the group's member list, wrong age group (process groups), or no QR because parent lacks My ChurchSuite access.
- Legacy Connect child check in is retired (31 May 2026). Use the Check-In app.

## Calendar and Bookings

- Event times not matching booking: edit each booked resource, apply to sequence if needed.
- Google Calendar not updating from iCal: test in Outlook, Google can lag up to a day.
- Cannot delete a booking: it has a paid online charge.
- Site specific public iCal feed is not possible, the public feed is all sites.

## Giving

- Donations not claimable: missing or mis-dated declaration. Fix the declaration, donations return to Unclaimed and are claimable next claim.
- Donate gift not Gift Aided: declarations from Donate are fund specific, cannot be "All funds" and cannot backdate 4 years.
- Bank import mismatch: only credits import, check the learned bank reference.

## API and embed

| Symptom | Fix |
|---|---|
| "API only supports JSON responses" | Send `Accept: application/json` and call the API from code, not a browser redirect. |
| 401 from token endpoint | Wrong client id or secret, secret disabled or deleted, user archived, API access disabled. |
| 403 or empty data | Missing scope or the API user lacks module or site permissions. |
| Rota slot data missing | Individual rota assignments are not documented in v2. Ministries, ministry members and unavailability are. |
| Embed shows nothing | Event or group not set to Show in embed, or the embed configuration filters exclude it, or old unrestricted URL used with the v4 script. |
| v1 key stops working | v1 is deprecated, switching off 1 August 2027. Migrate. |

## Decision guides

- Archive or delete? Archive to keep history and stop processing. Delete only when the person has no further lawful basis for retention. Delete is permanent.
- Fixed or smart tag? Fixed for a manually curated list, smart when membership should follow the data.
- Embed or API? Public website content: Embed. Anything with personal data: API v2 on a server.
- Unavailability or decline? Unavailability blocks all rotas for dates. Decline affects one rota date.
- Module User or Overseer? Overseers manage their ministry in My ChurchSuite without module access.
