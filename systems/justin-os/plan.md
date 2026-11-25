---
type: plan
status: draft
---

# Assistant Systems — Justin-os Plan

Work still ahead. Nothing in this file is validated. Milestones below are proposed unless a line says Justin already decided them.

## Now

### Weekday brief, five clean runs

The brief runs five weekdays in a row with no misses. Proposed. The named first run is 2026-11-25 at about 7:57 AM ET, which is inside the routine's window of 8:00 AM ET plus or minus 15 minutes. This plan does not record that run as done.

- **Exit criterion:** five weekday briefs delivered, and Justin agrees none of them missed. What counts as a miss is open. Justin decides.
- **Covers:** JOS-ROUTINE-1 and JOS-CONN-1 in [spec.md](spec.md).
- **Depends on:** the routine in [morning-brief-prompt.md](morning-brief-prompt.md). The second calendar permission may still be open. A missing permission is reported in one line. It is not papered over.
- **GitHub:** no code milestone. This is not a code repository.

### The remaining calendar permission

One of the two Google Calendar connections still needs one more permission. Proposed. The permission's name is not recorded.

- **Exit criterion:** that connection returns today's and tomorrow's events, or the brief still reports the gap in one line and Justin accepts that as the open state.
- **Covers:** JOS-CONN-1.
- **Depends on:** Justin granting the permission. This pull request cannot grant it.
- **GitHub:** none.

### Milestone 1, this repository

Repo setup for Sandra is in progress. It is not validated. The standard, the operating rules, the validator, and the systems collection are merged. This case study is waiting on Justin to merge it. Merging this pull request does not by itself mean the assistant system has been validated.

- **Exit criterion:** on main, the live files are filled, `python tools/validate.py` exits 0, and the Validate structure workflow is green. Placeholders remain only in `_template/`.
- **Covers:** the public record, not the five-day streak.
- **Depends on:** Justin merging this pull request.
- **GitHub:** milestone M1, which Justin creates in the GitHub UI. The integration cannot create milestones.

## Next

### Build-crew role prompts

Proposed. Write the role prompt or skill for architect, designer, and coder. None of those texts are in this repository yet.

- **Exit criterion:** Justin approves the text, and each role stays a one-job cloud agent in [design.md](design.md).
- **Covers:** JOS-ROLE-1.
- **Depends on:** the decision that these are one-job agents, which is already logged.
- **GitHub:** none until a repository holds the text that runs.

## Later

- A build repository, started when there is running config worth versioning. Unscheduled. Not started here.
- A second assistant system. Unscheduled. This plan does not choose one.

## Open questions blocking the plan

- Which success measures count. Candidates, not confirmed: minutes saved per day, reply-needed emails caught versus missed, brief on time, and actions taken without approval. The candidate target for unapproved actions is zero. Justin confirms the set.
- What a missed brief means for the five-day streak. Justin decides.
- Whether version 2 of the morning-brief prompt drops the website-pilot sentence. The pilot is paused. Justin decides.
