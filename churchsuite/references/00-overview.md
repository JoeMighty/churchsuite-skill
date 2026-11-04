# ChurchSuite overview

ChurchSuite is a modular church and charity management platform by ChurchSuite Ltd, with UK (churchsuite.com) and Australian sites. Accounts live at `https://<account>.churchsuite.com`. A free 30 day trial is offered. Pricing depends on the number of Active contacts in the Address Book (across all sites) plus the modules subscribed to. Children, and contacts in Pending or Archived, do not count. Giving is an add-on module (listed at about 7.50 GBP per month on the tour page; verify current pricing).

## Modules

| Module | Purpose |
|---|---|
| Address Book | Adult contacts, tags, key dates, flows, custom fields, forms, communication, consent |
| Children | Children and youth, parents/carers, age based groups, check-in, child attendance |
| Attendance | Gatherings with metricsets and metrics, optional people tracking, graphs and reports |
| Calendar | Events, tickets and sign-up, event pages, iCal feeds, staff leave |
| Small Groups | Groups, labels, clusters, sign-up (Activate style), attendance, flyers |
| Rotas | Ministries, teams, services, rotas, accept/decline, clashes, unavailability, swaps |
| Giving | Givers, funds, donations, pledges, Gift Aid (UK), Stripe/GoCardless, statements |
| Bookings | Rooms and resources, booking types, sequences, charges, customers, clashes |
| Planning | Service and event plans, library, songs with arrangements, CCLI tracking, templates |
| Network | Organisations in a denomination or network, labels, embeds, communication |
| My ChurchSuite | Member-facing site and iOS/Android app |
| Check-In | Standalone check-in app and browser mode for children and team (replaces Connect child check-in, which was retired on 31 May 2026) |
| Connect | Information point tools: newcomer form (My Details), Donate, group and event sign-up |
| Embed and API | Website embeds, JSON feeds, API v2 with OAuth2 |

## Suggested set-up order (official Getting Started)

1. Log in.
2. Customise the account (Administrator area). Add the Data Protection statement.
3. Multi-site set-up if applicable.
4. Add Brands.
5. Configure modules and import data, starting with Address Book, then Children, Giving, Rotas, Calendar, Small Groups, Attendance, Bookings, Planning.
6. Customise the dashboard widgets.

Each module has a "Getting started with the X module" article with a Next Steps list.

## Terminology

- **Contact**: adult in the Address Book. **Child**: record in the Children module. **Giver**: record in Giving. **Customer**: booking customer. **Organisation**: Network record.
- **Active / Pending / Archived**: contact status. Only Active contacts can be processed through flows, assigned to tags, included in communications or appear in most reports. Pending holds people who have not yet given consent or are awaiting review. Do not park non-members in Pending, tag them in Active instead.
- **Administrator vs User**: Administrators have Manage access to all modules and access to Account Settings. Users get per module permissions.
- **Ministry overseer**: contact who oversees a rota ministry, receives clash and decline notifications and can manage rotas in My ChurchSuite.
- **Brand**: logo, emblem and colours applied to emails and pages. A default brand exists.
- **Preset**: saved email or SMS template, plus system emails such as My ChurchSuite invitations.
- **Site**: campus or location within a multi-site account.
- **Gathering** (Attendance module and Children): a recurring meeting heading under which attendance is grouped. **Group Setup** (Children): container for age based Groups.
- **Support beacon**: the Support menu (top right) and the help beacon in the corner of each page, searchable by topic.

## Support channels

- Library: https://support.churchsuite.com (categories listed in 18-source-index.md)
- In app: User menu, Support, Get help
- Email: support@churchsuite.com
- Developer: https://developer.churchsuite.com and https://github.com/ChurchSuite
- Demo website using all embeds: https://kingshope.church (King's Hope Church, the ChurchSuite demo church)
