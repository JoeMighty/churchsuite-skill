<div align="center">

# ChurchSuite Skill

**An expert agent skill for [ChurchSuite](https://churchsuite.com), the church and charity management platform.**

Every module, administration, data protection, importing and exporting, plus the developer Embed and API v2 interfaces.

[![Licence](https://img.shields.io/github/license/JoeMighty/churchsuite-skill?style=plastic&label=licence&color=blue)](LICENSE)
[![Checks](https://img.shields.io/github/actions/workflow/status/JoeMighty/churchsuite-skill/checks.yml?style=plastic&label=checks)](../../actions/workflows/checks.yml)
[![Python](https://img.shields.io/badge/python-standard%20library%20only-3776AB?style=plastic&logo=python&logoColor=white)](churchsuite/scripts)
[![References](https://img.shields.io/badge/references-24%20files-success?style=plastic)](churchsuite/references)
[![Last commit](https://img.shields.io/github/last-commit/JoeMighty/churchsuite-skill?style=plastic)](../../commits)
[![Stars](https://img.shields.io/github/stars/JoeMighty/churchsuite-skill?style=plastic)](../../stargazers)

</div>

> Unofficial. Not affiliated with or endorsed by ChurchSuite Ltd. ChurchSuite is a trademark of its owner.

## What it covers

Address Book, Children and Check-In, Calendar, Small Groups, Rotas, Giving and Gift Aid, Bookings, Planning, Attendance, Network, My ChurchSuite and Connect, users and permissions, multi-site, brands and presets, communication and merge fields, CSV import and export, GDPR and retention, Embed and JSON feeds, API v2 with OAuth, recipes for common ministry scenarios and a troubleshooting guide.

## Install

The skill is the `churchsuite/` folder (a `SKILL.md` plus `references/` and `scripts/`).

**Claude Code (personal):**

```bash
git clone https://github.com/JoeMighty/churchsuite-skill.git
cp -r churchsuite-skill/churchsuite ~/.claude/skills/
```

**Claude Code (project):** copy `churchsuite/` into `.claude/skills/` in your repository.

**Claude.ai / other skill hosts:** zip the `churchsuite/` folder so that `SKILL.md` sits inside it, then upload it in your skills settings.

## Built for beginners too

New to ChurchSuite? The skill switches to a plain English, task first mode: it asks your role and goal, then gives numbered steps. It includes about 40 "How do I...?" playbooks, a glossary, a 30 day onboarding plan, role guides (admin, overseer, group leader, children's lead, treasurer, web volunteer), UK, Australia and US notes, ready to use templates in `assets/` (import CSVs, permission matrix, flow blueprints, smart tag recipes, presets, checklists, audit sheet), local checkers in `scripts/`, and workflows (`cs-onboard`, `cs-import-check`, `cs-audit`, `cs-gdpr`).

## Use

Ask naturally, for example:

- "How do I set up smart tags for newcomers in the last three months?"
- "Why is a rota swap blocked?"
- "Write a script that lists active contacts through the ChurchSuite API."
- "Plan a migration from Elvanto into ChurchSuite."
- "Draft a GDPR checklist for our ChurchSuite account."

## Layout

```
churchsuite/
  SKILL.md                      entry point and routing
  references/                   one file per area (00 to 23)
  assets/                       templates, CSVs, checklists
  workflows/                    cs-onboard, cs-import-check, cs-audit, cs-gdpr
  scripts/churchsuite_client.py API v2 client (standard library only)
  scripts/csv_preimport_check.py, giving_csv_check.py, merge_field_lint.py
  scripts/embed_example.html    minimal Embed JSON example
evals/                          30+ prompts and a scoring guide
.github/workflows/              monthly link check and basic checks
```

## Accuracy and updates

References were compiled from the public support library, developer site and ChurchSuite GitHub repositories in November 2026. ChurchSuite changes often. `references/18-source-index.md` lists article URLs for checking details. API details (base URL, token URL, client credentials grant, scopes) were confirmed from public sources. Rate limits and some response shapes are undocumented, so verify against https://developer.churchsuite.com.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Corrections with a source link are very welcome.

## Licence

MIT, see [LICENSE](LICENSE).

## Topics

Terms this skill is indexed under, matching the repository topics:

`agent-skills` `ai-agent` `ai-agent-skill` `ai-agent-skills` `charity` `chms`
`church` `church-management` `church-management-system` `churchsuite`
`claude-code` `claude-code-skill` `claude-code-skills` `claude-skill`
`claude-skills` `gift-aid` `ministry` `nonprofit` `python`
`reference-documentation`
