# Bookings

Manage internal and external bookings of rooms and resources, with customers, charges and online payment. Landing: 563. Getting started: 536.

## Concepts

- **Booking Types**: distinguish weddings, funerals, external hires, internal use. Types can have overseers who receive daily or weekly digests of new or amended bookings, and default Resources (added May 2025). Digests can be sent to the user email rather than the personal contact email (2025 update).
- **Resources**: rooms and equipment, with optional quantity (for example 20 chairs), overseers, and usage tab showing how often a resource is used.
- **Booked resources**: resources assigned to a booking, with setup and set down time outside booking times. Multiple resources can be added at once. Times visually flag when outside the booking times.
- **Customers**: booking customers with their own database, communication, merge duplicates, flows (Managing booking customers).
- **Planner**: overview of all bookings, Day view shows overlaps.
- **Task checklists** attach to bookings.

## Bookings workflow

1. Add booking (two step process: details, then resources).
2. Link to a Calendar event if relevant (Linking bookings and events).
3. Add resources, review clashes.
4. For sequences use Booking sequences (article 266): tick Add to sequence when adding resources, remove generated dates (for example term time only) or Add date for ad hoc sequences. Care when a booking sequence is linked to an Calendar event sequence.
5. Raise charges if external.

## Clashes (article 232)

Alerts when a resource is in use or quantity is exceeded. Users can approve a clash to continue (Administrators always can; clash approval can be set admin only). Approved clashes show yellow, expandable for detail, and appear in the Clashes report and Planner Day view. Setdown/setup overlap is a typical acceptable clash.

## Charges and payments

- Raise charges against single or sequence bookings: deposits, balances, instalments, ad hoc, refunds. Due dates, invoice numbers, visibility per booking (hide until approved). Charge history gives an audit trail.
- **Booking Prices**: reusable price list that auto calculates charges (March 2023).
- Send customers an online **booking page** showing details and charges.
- Online payment through **Stripe**, plus manual payment recording (cash, cheque, bank). Customisable payment confirmation email per booking type.
- Reports: Charges and Stripe Transfers. Reconcile via Viewing Stripe transfers.
- Bookings with paid online charges cannot be deleted (audit).

## Website

- **Booking enquiry form** and **free/busy resource planner** embeds. The planner uses anonymised booked resource JSON from the Bookings embed configuration so visitors can check availability before requesting.
- iCal feed of bookings available to Calendar/Bookings module users.

## API

Booked Resources JSON endpoint redesigned in February 2025. There is no resource or date filter on `/bookings/booked_resources` in API v2 (community tools fetch everything and filter client side). Scope name used by community tools: `bookings.read`.
