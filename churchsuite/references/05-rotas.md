# Rotas

Simple rota management with reminders, clash detection, unavailability and swaps. Landing: 561. Getting started: 524.

## Concepts

- **Ministry**: area of serving (can be duplicated). **Team** and **Role** sit under ministries. **Ministry overseers** are contacts with oversight who get clash, decline and unavailability notifications and can manage rotas in My ChurchSuite.
- **Services** and **rotas**: assign rotas to services. Add notes to rotas and services. Working with rotas once created has its own article.
- **Rota expiry reminders** and email/SMS reminders. Rota level reminder customisation was added in 2023. Merge fields `::roles::` and `::serving_date::` only work inside rota reminders.
- Sign up rotas: some rotas allow people to sign up themselves.

## Clashes (article 220)

Two types: **date clash** (serving on more than one rota at the same date/time) and **unavailability clash**. Shown red (date clash) or red strikethrough (unavailability or decline). Clash detection is a decision tool, not a barrier: you can still add people. Clash detection can be enabled or disabled per rota (Add rota or Edit rota pop up, and the equivalent in My ChurchSuite), useful where rotas deliberately overlap (for example Communion and Readings). Clashes and Unavailability tabs on a rota's View page list all clashes.

## Unavailability (article 378)

- Enable under Module Options, Unavailability, Edit. Adds an Unavailability section in the Rotas module and My Rotas.
- Unavailability blocks a person across all rotas for the date range, and creates a clash when someone adds or swaps them.
- Rota members add their own in My ChurchSuite (and for linked family members). Where this clashes with an existing serving, overseers of that ministry are emailed.
- Overseers and module users can add unavailability from date Actions, when adding Leave, or on the Unavailability section. History is kept and viewable by switching Past and Future.
- Best practice for members: add unavailability early and arrange a swap (rather than unavailability) for the coming Sunday.

## Accept / decline (article 581)

Optionally require rota members to accept or decline. A **decline** only clashes for that rota on that date (unlike unavailability which clashes across all rotas). Rotas can be sent from ChurchSuite (users) or from My ChurchSuite (overseers). Overseers get timely notifications of declines for future dates. Swapped in members are added with an Accepted status when accept/decline is on.

## Swaps (article 221)

- Members organise a swap relationally, then record it: My Rotas, serving Actions button, Organise swap. They choose who to swap with (only available people listed) and optionally a Return swap from that person's future serving dates in the same ministry. Save Changes updates the rota and sends confirmations and overseer notifications.
- Members cannot process a swap that causes a clash for the other person. In that case a module user or overseer must process it. Overseers can override swap clashes.
- Swaps can be disabled for members (overseers still can swap).

## My Rotas (My ChurchSuite)

Sections: Next Serving (next three months), Rotas, Unavailability, Rota Swaps, Rota Sign Up, All Rotas, Ministry Overseers. Email members from My Rotas to start swap discussions. Privacy settings control who can see whom. Admin side: Rotas module My ChurchSuite Options.

## API coverage

Core API v2 (per the public changelog, October 2026) includes `rotas/ministries`, `rotas/ministry_members` (sorted by ascending member ID by default, supports `order_by`), and `rotas/unavailability` with create (POST) and delete (DELETE) added in September 2026. Individual rota slot assignments and dates are not documented as endpoints, so for "who is serving this Sunday" use rota iCal feeds, CSV export or Planning plan items. Check the changelog before relying on this, it changes often.

## Planning link

Plan items can link to rotas so plans update automatically when rotas change.
