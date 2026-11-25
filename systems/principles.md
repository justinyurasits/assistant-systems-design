---
type: principles
status: current
---

# Assistant Systems — Principles

Lessons from the 2026-11-24 setup. A principle is added only when an incident teaches it. The incidents are written up in [justin-os/build-log.md](justin-os/build-log.md).

## 1. Check what already exists before scoping a build

Before a build is scoped, look at the work already on the relevant branch and in the design record. A new scope that skips that look repeats the miss.

- **Learned from:** On 2026-11-24 a website pilot overlapped an existing v2 site. The overlap was found by checking v2 after the architect had started. Design pull request #76 in justinyurasits/design was closed unmerged and its branch was deleted. main and v2 in that design repo were not changed. Recorded in [justin-os/build-log.md](justin-os/build-log.md).
- **Rules that follow:** Read what is already on the branch and in the design docs before writing the scope. If the design is silent, ask. Do not open a build on top of work that was not read.
- **Enforced in:** Justin's review before a build is scoped. [AGENTS.md](../AGENTS.md) requires an approved issue, read first, and a stop when the design is silent. [tools/validate.py](../tools/validate.py) does not check this.

## 2. Connector setup is part of the build and needs its own checklist

Connecting an account is part of the build, with its own checklist, not a step that happens off to the side.

- **Learned from:** On 2026-11-24 the browser blocked connector pop-ups, a second sign-in was started before the first was finished, and one calendar connection was left short one permission. Recorded in [justin-os/build-log.md](justin-os/build-log.md).
- **Rules that follow:** Allow the browser to show the pop-up. Finish one account sign-in before starting another. Check permissions per account. Do not name the account in this public repository.
- **Enforced in:** A connector-setup checklist that is part of the build. The checklist file is not in this repository yet. Justin decides when it is added and where it lives. The checks already named are pop-ups, one sign-in at a time, and permissions per account. [tools/validate.py](../tools/validate.py) does not check them.

## 3. Say which helpers are standing assistants and which are one-job cloud agents

When a helper is described, say whether it is a standing assistant or a one-job cloud agent.

- **Learned from:** On 2026-11-24 the architect had no icon in the left panel, and Justin read that as a standing bot. The coder caused the same confusion later. That agent lives on cursor.com. Recorded in [justin-os/build-log.md](justin-os/build-log.md).
- **Rules that follow:** Name the kind of each helper, and where Justin can see it. Do not leave the kind to be inferred from a panel icon.
- **Enforced in:** [justin-os/design.md](justin-os/design.md), reviewed by Justin before merge. [tools/validate.py](../tools/validate.py) does not check it.

## 4. A brief's sections follow the work that shows up

A brief's sections have to follow the work that actually shows up, not the sections that were planned in advance.

- **Learned from:** On 2026-11-24 most of the real inbox volume was not business mail. A brief planned around business mail would have missed how the inbox actually looked. Personal mail is its own short section. Recorded in [justin-os/build-log.md](justin-os/build-log.md).
- **Rules that follow:** Write the brief's sections from the mail that arrives. Keep personal mail separate from business mail. Do not keep a section only because it was planned.
- **Enforced in:** Justin's review of brief.md, and of [justin-os/morning-brief-prompt.md](justin-os/morning-brief-prompt.md), before merge. [tools/validate.py](../tools/validate.py) checks that a project README has the sections from the template. It does not check that a brief's sections match the work.

## 5. Copy the proven standard and change only what is tool-specific

Keep the document standard that already works. Change the parts that exist because of a different tool. Do not rewrite the file set from scratch.

- **Learned from:** On 2026-11-24 this repository forked justinyurasits/design STANDARD.md revision 61. The sync-from-chat machinery was the tool-specific part that was dropped. AGENTS.md is the operating-rules file in place of the other tool's file. Recorded in [justin-os/build-log.md](justin-os/build-log.md).
- **Rules that follow:** Port the file set, the one-job rule, and the front matter. Drop or rename only the piece that does not belong. Say, in the standard's change history, what was dropped.
- **Enforced in:** [STANDARD.md](../STANDARD.md), which states the fork and that upstream changes are adopted only on purpose. Justin reviews any further port.

## 6. Know the integration's permission limits before the step that needs them

If an integration cannot do a step, plan the human step before starting. Do not discover the limit in the middle of the work and invent a workaround that the integration will reject.

- **Learned from:** On 2026-11-24 creating a GitHub milestone failed. The API returned 403 to the integration, and there was no working tool for it. Justin creates milestones in the GitHub UI. Recorded in [justin-os/build-log.md](justin-os/build-log.md).
- **Rules that follow:** Before a step that needs a GitHub write the integration may not have, name the human who does that step. Do not block the rest of the work on a call that is known to be forbidden.
- **Enforced in:** [AGENTS.md](../AGENTS.md), which keeps GitHub read-only except an approved issue and branch, and [justin-os/plan.md](justin-os/plan.md), which says Justin creates milestones in the GitHub UI. [tools/validate.py](../tools/validate.py) does not check integration permissions.
