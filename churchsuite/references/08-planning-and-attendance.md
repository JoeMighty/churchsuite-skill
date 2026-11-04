# Planning and Attendance

## Planning module (landing 564, getting started 492)

Produces plans for the running order of a service, event or booking: what happens, when, and who does it.

- **Plans** link optionally to services (Rotas), events (Calendar) and bookings (Bookings).
- **Library**: reusable items categorised by Types (for example Song, Reading, Heading). Types are customisable (Planning, Types). Items can have linked files (file storage is currently Planning only).
- **Songs** with multiple arrangements: transposable chord charts, lyric charts, Spotify and video links.
- **People**: assign people to plan items ad hoc, or link items to rotas by criteria so plans update when rotas change. Communication and sharing recipients derive from the people linked to items.
- **Templates**: save a great plan as a template and build plans from it.
- Drag and drop reorder, comments, important notes, durations. Note categories (for example "People") can be added to items.
- **Publish and share** a people facing plan page via link, viewable on phones.
- **CCLI tracking and reporting** for song usage and annual returns. Usage of any library item is tracked over time.
- Export and share to **MediaShout** and other third party services (Support for other third party services).
- Live progress: see where the plan is when running in real time.
- Community tool: hussra/churchsuite-plan-viewer prints plans using templates. It works best if you create a plan item type named "Heading".
- Planning data is available through Core API v2 (read) but not via Embed.

## Attendance module (landing 663, getting started 657)

Core repository for gathering attendance data.

- **Gatherings**: headings under which attendance for each date is grouped, totalled and reportable. Multiple gatherings can have data on the same date, with an On this date widget.
- **Metricsets and Metrics**: the statistics collected (number and currency values) for each gathering. Gatherings have preset metricsets which can be edited and deleted. You can move metrics between metricsets, move metricsets between gatherings, archive and reactivate (article 733).
- **People tracking** (optional per gathering): record which Address Book contacts attended (article 658). Enables engagement views such as families who have not been for a few weeks.
- **Reports** (rebuilt September 2024): a graph generator compares any metric from any gathering against any metric from another, and a second report for drilling into data and trends.
- Configure a gathering for Check-In (child group attendance from Check-In lives in the Children module and does not auto populate Attendance module metrics: populate them manually with children's totals if wanted).
- Use cases: answering Trustees' "how many", Church of England Worshipping Community statistics (case study 709 uses smart tags, fixed tags, key dates and custom fields).
