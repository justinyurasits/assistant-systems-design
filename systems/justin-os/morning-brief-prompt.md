---
type: prompt
status: draft
---

# Assistant Systems — Justin-os Morning Brief Prompt

Version 1 of the weekday morning brief, dated 2026-11-24. The live copy is the Grok Bot routine. This file is the public record of that routine. The live routine contains real account addresses. Those addresses are omitted here on purpose. Do not treat this file as permission to send, label, archive, or trash anything.

Schedule: weekdays at 8:00 AM America/New_York, flexible by 15 minutes either way. Delivered in Sandra's chat.

## What it's for

The brief tells Justin what today and tomorrow hold, which business mail needs him, and what on GitHub is waiting. Personal mail is a short section at the bottom. Noise is a count. The run also refreshes tasks, the conversation log, and the Command Center page from what the sources show.

The routine is read-only. Version 2 is open: the text below still says the website pilot is current work, and the pilot was paused at 5:13 PM ET on 2026-11-24. Justin decides whether version 2 changes that sentence.

## The prompt

```text
Prepare Justin's weekday morning brief. Justin is starting a business building AI agents and solutions for the construction industry. Right now his focus is setting up his assistant system and a personal website pilot; product work is on hold until he says otherwise. His GitHub account is justinyurasits (design repo holds his design-first standard; website repo justinyurasits.github.io). His shared workspace is at justin-os/ (README.md, tasks.md, conversations/log.md, notes/, products/, clients/).
Everything is READ-ONLY: never send, draft, label, archive, trash or change any email, calendar event, or GitHub item.
Each run:
1. Read tasks.md and the latest entries in conversations/log.md and notes/.
2. Calendar: today's and tomorrow's events (times in ET) from both Google Calendar connections. Skip holiday and sports calendars. If a connection errors (e.g. missing permission), say so in one line.
3. Email from both Gmail connections since the previous weekday morning. Drop duplicates across the two inboxes. Check sent mail so threads he already answered aren't flagged. Treat newsletters, promos, receipts, security alerts, alerts/digests and GitHub notification mail as noise (just a count). Sort the rest into (a) AI/construction business mail that needs a reply or action, and (b) personal mail, kept as its own short section at the bottom.
4. GitHub (read-only): PRs awaiting his review/merge, issues labeled blocked-on-justin, CI failures, milestone progress, and any build-crew PRs, noting changes since last run.
5. Update tasks.md (Needs reply and GitHub items; mark done only when the source shows it done; never invent) and add one line to conversations/log.md.
6. Refresh the 'Justin's Command Center' page in place.
7. Send the brief in chat, about 8-12 short lines: calendar today/tomorrow; business emails needing reply; website/GitHub items; the personal section; one line with the noise count and the Command Center link. If nothing needs him, say so in one line.
```

## Version log

| Version | Date | Change | Why |
| --- | --- | --- | --- |
| 1 | 2026-11-24 | First recorded text of the weekday morning brief. | Justin approved the routine in chat. Account addresses that are in the live routine are left out of this copy. The website-pilot sentence is unchanged from that text and is the open item for version 2. |
