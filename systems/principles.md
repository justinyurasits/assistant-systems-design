---
type: principles
status: current
---

# Assistant Systems — Principles

Lessons from the 2026-11-24 setup. A principle is added only when an incident teaches it. No further principles are recorded here.

## 1. Check what already exists before scoping a build

Before a build is scoped, look at the work already on the relevant branch and in the design record. A new scope that skips that look repeats the miss.

- **Learned from:** On 2026-11-24 a website pilot overlapped work already on the v2 branch of the site repo. Design pull request #76 was closed unmerged.
- **Rules that follow:** Read what is already on the branch and in the design docs before writing the scope. If the design is silent, ask. Do not open a build on top of work that was not read.
- **Enforced in:** Justin's review before a build is scoped. [AGENTS.md](../AGENTS.md) requires an approved issue, read first, and a stop when the design is silent. [tools/validate.py](../tools/validate.py) does not check this.

## 2. Connector setup is part of the build and needs its own checklist

Connecting an account is part of the build, with its own checklist, not a step that happens off to the side.

- **Learned from:** On 2026-11-24, browser pop-up blocking during connector setup. The rule that follows from that setup is to finish one account sign-in before starting another.
- **Rules that follow:** Allow the browser to show the pop-up. Finish one account sign-in before starting another. Do not name the account in this public repository.
- **Enforced in:** A connector-setup checklist that is part of the build. The checklist file is not in this repository yet. Justin decides when it is added and where it lives. The two checks already named are the browser card and finishing one sign-in before the next. [tools/validate.py](../tools/validate.py) does not check them.

## 3. Say which helpers are standing assistants and which are one-job cloud agents

When a helper is described, say whether it is a standing assistant or a one-job cloud agent.

- **Learned from:** On 2026-11-24 there was confusion when an architect agent had no icon in the left panel.
- **Rules that follow:** Name the kind of each helper in the component design. Do not leave the kind to be inferred from a panel icon.
- **Enforced in:** The component design.md, reviewed by Justin before merge. No component is in this folder yet, so the check has not been applied to a file here. [tools/validate.py](../tools/validate.py) does not check it.

## 4. A brief's sections follow the work that shows up

A brief's sections have to follow the work that actually shows up, not the sections that were planned in advance.

- **Learned from:** The 2026-11-24 setup. Brief sections had been planned in advance, and they were not the sections the work produced.
- **Rules that follow:** Write the brief from the work in the issue. Drop a planned section that the work did not produce. Do not keep a section only because it was planned.
- **Enforced in:** Justin's review of brief.md against the work in the issue, before merge. [tools/validate.py](../tools/validate.py) checks that a project README has the sections from the template. It does not check that a brief's sections match the work.
