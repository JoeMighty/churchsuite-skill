# Calendar

Create events, sell tickets or take sign ups, publish event pages, subscribe to iCal feeds and manage staff leave. Support landing article: 557.

## Event set-up topics

- **Categories**: group events, drive colours and category specific iCal feeds.
- **Questions**: custom questions on sign up.
- **Tickets**: free or paid ticket types, capacity. Online card payments go through Stripe, reconcile with the Stripe Transfers report.
- **Visibility and status**: Show in My ChurchSuite, Show in embed (public). Internal only events are excluded from public embed and JSON feeds.
- **Importing events** from CSV.
- **Linking bookings and events**: event details populate the booking. Mismatches between booking times and booked resources can be identified and fixed by editing each booked resource.
- **Multi date event sequences**: courses and repeating events. Changes can be applied across the sequence.
- **Online events**, **using brands**, **promoting events on social media**.
- Confirmation emails on sign up include event image, key details, tickets purchased and a calendar attachment. Resend confirmations from the event action menu. Admins can add people to the sign up list directly (existing contacts or visitors).
- Removing a paid sign up needs a double confirmation. Processing refunds and managing cancellations have their own articles.

## Event management

- **Event check-in** and **event sign-up at your information point** (Connect).
- Event pages are auto generated.

## iCal feeds (article 100 and 108)

- Public embed feed for all public events (all sites, not site specific): `webcal://<account>.churchsuite.com/ical/embed.ics`.
- Calendar and Bookings module users: Calendar page, bottom, Subscribe to feed (iCal). Category feeds via the Categories section. Includes events, bookings and leave depending on selection.
- Google Calendar: subscribe by URL. If changes do not appear, test in Outlook to isolate the issue. Google can lag.
- My Rotas iCal feed: ChurchSuite refreshes every 24 hours so swaps may not show immediately. Android cannot subscribe to iCal natively (use Google Calendar). Desktop Outlook cannot subscribe, use Outlook on the web.

## Staff leave

Annual leave and sick leave management with allowances, requests and approval. Leave can create rota unavailability (Adding unavailability when adding Leave).

## Embedding

Calendar embed (grid view), event feeds and individual event pages are embeddable. Calendar embed configurations live in the Calendar module's Embed tab and are what the JSON feed and the `@churchsuite/embed` script use. See 15-developer-api-and-embed.md.
