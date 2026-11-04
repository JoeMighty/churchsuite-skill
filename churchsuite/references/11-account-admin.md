# Account settings and billing (Administrator area)

Support category: Account Settings & Billing (44 articles). Only Administrators can open Account Settings.

## Users and permissions (article 126)

- Two user types: **Administrators** (full Manage access to every module, plus Account Settings: Users, User Groups, Modules, Files, Profile, Sites, Presets, Brands, Integrations, Administrator reports) and **Users**.
- Per module permission: **None, Use, Write, Manage**. Use and Write cover day to day work. Manage also changes module settings, which affect all module users. A separate **Connect** permission allows Connect and Check-In apps.
- **Sites**: per user permitted sites (single, multiple, or All sites). Users can only add, import, edit, duplicate, merge, move, archive or delete data for permitted sites.
- Duplicate a user to copy signatures, user groups, sites and module permissions. Archive or delete users. Permissions report is site specific.
- **User Groups** and **Restricting feature visibility and access to reports** limit sensitive features.
- Add user steps: User menu, Settings, Users, Add user.

## Security

- User security and passwords, **multi-factor authentication** (strongly recommended, admin accounts may require it), **module passwords** (extra password on sensitive modules such as Giving), granting Support Team access (time limited).
- Information is encrypted at rest in UK data centres.

## Multi-site (article 216)

Add sites under Account Settings, Sites. Assign user site permissions, assign details (people, groups, events) to sites. A site shares the umbrella account's settings, so the same data protection notice and data protection contact apply. People can be assigned to multiple sites or All sites (users with All sites permission only). Location reporting, My ChurchSuite and Check-In behave per site. Import into a multi-site account needs a site column or selection. Deleting sites has consequences, check the article first.

## Profile and customisation

- Customising your account (article 62): logo, emblem, colours, dashboard widgets.
- **Profile**: account contact, billing contact, **data protection contact**, Data Protection statement (privacy notice) upload. Several features (such as "Forget me") only appear once the statement is added.
- **Brands**: multiple brands for email and pages, default account brand.
- **Presets**: preset emails, preset SMS, system email templates. Personalising email signatures. Sending emails from a shared email address.
- **Files**: account file store.
- **Modules**: add or remove modules, module settings via cogwheel.
- **API**: Enable API access per user, API Secrets tab (user creates, max two per user), OAuth Apps tab (see 15-developer-api-and-embed.md).

## Integrations

BulkSMS, Twilio (SMS), Textlocal (SMS), GoCardless, Stripe (cards, used by Giving, Calendar tickets and Bookings charges), Mandrill (email, supports multiple domains), Elvanto importer, Podcast feed, MediaShout and other planning services, and Zapier style tools via the API.

## Billing

Setting up your ChurchSuite payment subscription, account management, billing contact. Billing is based on Active Address Book contacts plus modules. Archive or delete leavers to control cost.

## Logs and retention (article 155)

- Automated daily backup of all account data, encrypted backups kept for 30 days then overwritten.
- Deleted data log viewable by admins.
- Email errors older than 6 months are removed. Login logs older than 3 years are removed. Visitor children not checked in beyond the retention setting are removed.
- See 14-data-protection.md.

## Admin reports

User permissions, logins, communication log (Recent Activity in Administrator, Profile).
