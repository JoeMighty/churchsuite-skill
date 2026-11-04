# Network module

Relationship management for organisations within a network, church movement or denomination, plus partner charities. Support category: "Network" (11 articles).

## Capabilities

- Add or import **Organisations** (churches, charities) with no limit on number or type.
- **Labels** group or categorise organisations, useful for targeted communication and filtered reports.
- **Key dates** track organisation engagement over time. **Custom fields** hold extra details.
- **Targeted communication** to organisation members based on roles and other factors.
- **Multi-site**: segment one or more networks, or use labels.
- **Reports** and visualisation of how the network develops.
- **Embed**: lists or maps of organisations for your website, driven by Network embed configurations and updated automatically from ChurchSuite.

## Developer notes

- The Network Organisations JSON feed uses a paginated response with labels, sites and brands returned separately (embed script v3, for efficiency with large datasets). In embed script v4 and v5 the Network organisations feed was disabled pending redesign, so check the changelog at https://www.npmjs.com/package/@churchsuite/embed before building.
- Site addresses include latitude and longitude keys in newer embed JSON.
- Network is part of the Embed Configurations set (Calendar, Bookings, Small Groups, Network).
