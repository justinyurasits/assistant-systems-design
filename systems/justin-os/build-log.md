---
type: build-log
status: current
---

# Assistant Systems — Justin-os Build Log

What happened, and what it changed. This entry is the setup day, not a transcript.

## 2026-11-25 — calendar list permission

- **Did:** At about 4:56 PM ET, Justin re-approved the Google Calendar sign-in and ticked every box on the consent screen. Checked right after: the calendar list returns, and the primary calendar is at owner access. No account address is recorded.
- **Broke:** Since setup, one Google Calendar connection was missing the permission to see that account's list of calendars. The consent screen lets individual permissions be unticked, and the first sign-in came back with that one unticked. The morning brief on 2026-11-25 reported both calendars readable from event reads, while listing calendars still failed. A partial permission can look healthy.
- **Learned:** Tick every box on a connector consent screen. Verify a connector with a call that needs each permission, such as listing calendars, not only the call that happened to work. This is JOS-CONN-1. The checklist lesson is in [../principles.md](../principles.md).

## 2026-11-24 — justin-os setup

- **Did:** Stood up justin-os. Sandra is the standing chief-of-staff assistant: notes, tasks, a conversation log, a weekday morning brief around 8:00 AM ET, and drafts in this repository. Product Lead is a second standing assistant for per-product and per-client vision. Architect, designer, and coder run as Cursor cloud agents, one job each. The shared workspace on Sandra's computer is justin-os/, with README, tasks, conversations/log, notes/, products/, and clients/. The brief refreshes a Command Center page. Connectors attached that day: GitHub through the Cursor GitHub app, two Gmail accounts, two Google Calendar accounts, and Google Drive. At the end of setup, one calendar connection was missing the permission to list calendars. That was fixed on 2026-11-25. The public design for the practice went into this repository. STANDARD.md forks design revision 61. Documents are pull requests, not a sync from chat.
- **Broke:** Connector connect cards and links did not open, because the browser blocked pop-ups. Allowing pop-ups for cursor.com fixed that. A duplicate, half-signed-in Gmail account was left behind and had to be removed. The address is omitted. The architect had no icon in the app's left panel, which confused Justin. It is an ephemeral cloud agent, not a standing bot. The same confusion came later with the coding agent, which lives on cursor.com. The website pilot's first scope overlapped an existing v2 site. That was found by checking v2 after the architect had started. Design pull request #76 in justinyurasits/design was closed unmerged and its branch was deleted. main and v2 in that design repo were not changed. The new repository was first created with a typo in its name, caught through the GitHub API, and renamed. The mistyped name is omitted. Cursor's GitHub app still showed a stale view of the new repo with access set to all repositories. Re-requesting the connection fixed it. Creating a milestone failed: the integration returned 403, and there was no working tool for it. Justin creates milestones in the GitHub UI.
- **Learned:** Check the existing branch before scoping a build. Connector setup needs its own checklist: pop-ups, one account at a time, and permissions per account. Say which helpers are standing bots and which are one-job agents, and where Justin can see each. Most of the real inbox volume was not business mail, so the brief's sections follow the mail, not the plan. Copy the proven standard and change only what is tool-specific. Know an integration's permission limits before the step that needs them, and plan the human step. The principles that record these are in [../principles.md](../principles.md). The decisions are in [design.md](design.md).
