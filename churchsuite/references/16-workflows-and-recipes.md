# Workflows and recipes

Practical patterns combining modules. Case study category on the support site has 19 articles; titles include those referenced here.

## Newcomer integration

1. Embed or Connect "My Details" form on the website and information desk. Form submissions land as Pending or Active depending on settings and person detection matches existing records.
2. Create a Flow: Stage 1 welcome (send preset email, add key date "First Visit"), Stage 2 follow up call (assign a user), Stage 3 invite to group (preset email with link), Stage 4 membership class.
3. Smart tag "Newcomers last 3 months" using the First Visit key date for reports and rota planning.

## DBS and safer recruitment

Key date "DBS check" with expiry. Flow with a stage that notifies the office as expiry approaches. Smart tag for volunteers with an expiring DBS. Use note visibility to restrict sensitive notes. See article 637 (safer recruitment). Australia: Working With Children Checks (703) and Safe Ministry (719).

## Church of England Worshipping Community statistics (case 709)

Smart tag combining: people who attend services (Attendance people tracking or a custom field), fixed tag for housebound, key date for home communion, fixed tag for those in care homes, and Children module equivalent. Report the tag count.

## Pastoral care (case 457)

Tags and key dates for visits, flow for follow up, notes with restricted visibility, overseers assigned.

## Subscriber mailing lists (case 590)

Contacts tagged as non members, communication options limited to email, a dedicated preset email and unsubscribe handling through My Consent.

## Holiday club and parent and toddler groups

Child groups per age band, Check-In session templates, QR check in, consent smart tags for photo and video, end of club report from child attendance.

## Event with tickets and payments

Calendar event with sign up and ticket types, Stripe connected, optional booking linked event for room and resource allocation, confirmation email, event check in on the day, Stripe Transfers report to reconcile.

## Hire of premises

Bookings: customer, booking type with default resources, booking prices, raise charges, send booking page, accept online payment, task checklist for set up, Clashes report, free/busy embed on the website.

## Service planning

Rotas set serving teams, Planning plan linked to the service and rota with people items, templates for recurring services, publish the plan link to the team, CCLI report at year end.

## Small groups season

Labels for group types, clusters per pastor, sign up open via website embed, attendance reminders switched on, Missing Attendance report monthly, Monthly Engagement graph for leadership.

## Giving drive

Fund for the project, Donate embed, pledges for committed givers, Declarations Missing report then flow to ask for Gift Aid declarations, statements emailed at year end.

## Year end tidy

Archive leavers, delete data past retention, review users and permissions, remove unused API secrets, export CSV backups, update the data protection statement.

## Website integration (typical for a developer)

1. Create embed configurations in Calendar and Small Groups.
2. Use the `@churchsuite/embed` script or fetch the JSON in a build step and cache it.
3. For member only data build a server side app with API v2 client credentials, minimal scopes, and cached results.
4. Stripe and Donate remain inside ChurchSuite, embed the Donate form rather than rebuilding it.
