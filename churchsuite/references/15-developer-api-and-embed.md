# Developer: Embed, JSON feeds and API

Sources: https://support.churchsuite.com/article/454-developer-api, https://developer.churchsuite.com, https://github.com/ChurchSuite/churchsuite-api (OpenAPI 3.0 specs), https://github.com/ChurchSuite/embed-json-script, https://www.npmjs.com/package/@churchsuite/embed, demo site https://kingshope.church.

Always check developer.churchsuite.com for current endpoints before writing production code. ChurchSuite states its API documentation is "in flux" and changes may break applications.

## Which option to use

| Need | Use |
|---|---|
| Show events, small groups, booked resources or network organisations on a website | **Embed** (iframe HTML) or **Embed API / JSON feeds** |
| Read or write other module data (people, forms responses, plans, metricsets, giving...) | **Core API v2** (OAuth2) |
| Something v2 cannot do yet | Legacy API v1 (deprecated, see below) |
| Let members log in to your own app with ChurchSuite credentials | OAuth2 server with an OAuth App |

## Embed (no code)

Embeddable features: My Details (newcomer form), Donate, Small Groups (list or map), Calendar (grid), Event feeds, Event pages (sign up form only), Forms, Free/busy resource planner, booking enquiry form, Network organisations. Each is configured inside ChurchSuite, which generates HTML to paste into your site. Content stays current as ChurchSuite data changes.

## Embed API and JSON feeds (public, read only, no personal data)

- Driven by **Embed Configurations** in the module settings (Embed tab) of Calendar, Bookings, Small Groups and Network. Non technical staff change filtering in ChurchSuite without touching site code.
- Respects "Show in embed" visibility, so internal only events and groups are excluded.
- Publicly accessible to anyone with the URL.
- Public URL pattern (from the community WordPress plugin docs): `https://<account>.churchsuite.com/-/calendar/<embed-config-uuid>/json`. Older unrestricted pattern `https://<account>.churchsuite.com/embed/calendar/json?num_results=3` is the v1 style feed.
- Embed JSON script `@churchsuite/embed` (MIT, Alpine based). Version 4 and 5 require an embed configuration created in ChurchSuite, the unrestricted public feed is no longer usable with them. Classes include CSBookedResources. Changelog highlights: 5.2.5 (March 2025) documented the Small Groups groups endpoint, 5.1.0 (Feb 2025) Booked Resources and Calendar redesigns. Some module feeds were disabled in v4 pending redesign (SG Groups, NE Organisations, BO Booked Resources) and have since been reintroduced progressively.
- Community WordPress plugins: Blocks for ChurchSuite, Integration for ChurchSuite, Javascript Integration for ChurchSuite.

## Core API v2

- **Private**, authorised with OAuth2, access to all account data including personal data. Read endpoints cover Account, Address Book, Attendance, Bookings, Calendar, Children, Giving, Network, Planning, Rotas and Small Groups. Write endpoints (POST, PUT, DELETE) have been added module by module and keep arriving (see the changelog).
- **Base URL**: `https://api.churchsuite.com/v2`. Always send `Accept: application/json`. A browser redirect to the API returns "This API only supports JSON responses; check your Accept header".
- **Token URL**: `https://login.churchsuite.com/oauth2/token`. CharitySuite accounts use `https://login.charitysuite.com/oauth2/token`.
- **Grants** (confirmed at developer.churchsuite.com/auth, Nov 2026): both Client Credentials and Authorisation Code are supported. Client Credentials is for server side apps acting for themselves: POST to the token URL with HTTP Basic auth (client id as username, secret as password), `Content-Type: application/x-www-form-urlencoded`, `grant_type=client_credentials` and a `scope`. Authorisation Code is for apps users log into: authorise at `https://login.churchsuite.com/oauth2/authorize`, token at `.../oauth2/token` (CharitySuite uses login.charitysuite.com). OIDC login is also offered. The response has an `access_token`, used as `Authorization: Bearer <token>` with `Accept: application/json`.
- **API user setup (client credentials)**: an admin creates a user with minimal permissions and clicks Enable API access (More menu). Then log in as that user, My profile, Secrets tab, copy the identifier and create a secret. A scope is required when requesting a token.
- **Scopes** (full list): `full_access`, `account` (account/info), `user` (account/users/current), `brands.read`, `profile.read`, `usergroups.read`, `users.read`, and `<module>.read` / `<module>.write` for addressbook, attendance, bookings, calendar, children, giving, network, planning, rotas, smallgroups. Scopes are always limited by the user's own permissions, whatever the token says. Example: `scope=user addressbook.read`.
- **Pagination**: many endpoints return a `pagination` object next to `data`. Default 50 per page, max 250 with `per_page=250`, page with `page=2`. Other common params: `order_by` (`field:direction`), `site_ids[]`, `ids[]`, `status`, `q`, `tag_ids`.
- **Rate limit**: 120 requests per 60 seconds per account on the Core API, resets each minute. Over the limit returns 429 with a `Retry-After` header: back off. 5xx: retry with exponential backoff and check the status page.
- **Money**: amounts are integers in the minimum currency unit, so GBP 150.53 is `15053`.
- **Partial updates**: since Sept 2026 `PUT addressbook/contacts/{id}` and `PUT children/children/{id}` no longer require every field.
- **Examples of endpoints named in the changelog**: `addressbook/contacts`, `children/children`, `children/group_setups`, `bookings/bookings`, `bookings/customers`, `bookings/resources`, `bookings/booked_resources`, `calendar/events`, `calendar/signups`, `calendar/labels`, `giving/givers`, `giving/donations`, `giving/declarations`, `giving/claims`, `giving/funds` (create, update, delete), `network/organisations`, `network/members`, `planning/plans`, `planning/plan_items`, `rotas/ministries`, `rotas/ministry_members`, `rotas/unavailability`, `smallgroups/groups`, `smallgroups/members`, `attendance/gatherings`, `account/sites`, tags, key_dates and flow tracking endpoints, and label management (`<module>/labels`) for Calendar, Network and Small Groups.
- Note: the support article 454 still says v2 covers all modules except Rotas, but the `rotas.read` scope and changelog show rota endpoints exist. Individual rota slot assignments are still not documented. Booked resources have no resource or date filter, so filter client side. Cache responses and respect the rate limit above.
- The public changelog at https://github.com/ChurchSuite/churchsuite-api/blob/master/CHANGELOG.md (versions 2.x, several releases a month) and the OpenAPI specs in that repository are the authoritative source. Re-read them for current endpoints.

### Creating API credentials (in ChurchSuite)

1. Administrator opens Account Settings, Users, the target user, More actions, **Enable API access**. A notice goes to the data protection contact.
2. The **user themself** logs in, opens their profile, **API Secrets** tab, **Add secret**, names it (for example "Website Member Area"), confirms their password. The Client Identifier and Client Secret show **once**. Save them securely.
3. A user may have up to two secrets. Secrets can be disabled (reversible) or deleted (permanent).
4. Use a dedicated user with minimum module and site permissions for the application.
5. Disabling API access, archiving or deleting the user blocks their credentials immediately.

### OAuth Apps (Authorisation Code grant)

Settings, **OAuth Apps** tab, add application with a redirect URL. Secrets are added on the app's view page. Edit or delete later (deletion is destructive). Users need not have API enabled to use OAuth Apps.

## Legacy API v1 (deprecated)

Header auth: `X-Account` (subdomain), `X-Application` (app identifier), `X-Auth` (API key from support or OAuth), `Content-Type: application/json`, base `https://api.churchsuite.com/v1`, for example `/addressbook/contact/1`, `/children/child/1`. The v1 API is **deprecated and will be turned off on 1 August 2027**. All applications should migrate to v2. v1 access must be requested via the account contact emailing support with a dedicated user profile that has only the Use or Write permissions required.

## Security and good practice

- Keep secrets in environment variables or a secret manager, never in source control or client side JavaScript.
- Call the API from a server, never expose client secrets in a browser.
- Request the narrowest scopes. Prefer read only.
- Cache responses, respect rate limits, and paginate.
- Do not store personal data longer than needed, and update the privacy notice if you add an external processor.
- Test against a trial or sandbox account before production.

## Tools in this repo

`scripts/churchsuite_client.py` is a dependency light Python client for client credentials auth and paginated GETs. `scripts/embed_example.html` shows a minimal fetch of an Embed JSON feed.
