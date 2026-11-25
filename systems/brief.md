---
type: brief
status: draft
---

# Assistant Systems — Brief

2026-11-24 · Justin

Assistant Systems is a collection of independent assistant-system case studies in this public repository. It is not one product. The outcome is a public record of those case studies: methods and decisions, written here by pull request.

## 1. Customer

The collection is for the owner's practice of designing assistant systems. The assistant drafts the documents. The owner reviews and merges them. It is not for product work, and it is not a place for personal or client data.

## 2. The painful moment

The practice is the response to the 2026-11-24 setup, recorded in [principles.md](principles.md). A website pilot overlapped work already on the v2 branch of the site repo. Connector setup hit browser pop-up blocking, and one account sign-in has to finish before another starts. There was confusion when an architect agent had no icon in the left panel. Brief sections planned in advance did not match the work that showed up. A single scene with a cost in time or money is not recorded. That gap is under Open.

## 3. What it replaces

These case studies are recorded in this repository. Product work stays in justinyurasits/design. The collection is grouped the way agents is grouped there: independent builds, with no product spec and no architecture. A prior tool or habit, beyond that split, is not named. That gap is under Open.

## 4. Goals and how we'll know

| Goal | Measured by | Target |
| --- | --- | --- |
| The folder stays a collection of independent case studies, not a product | No product-spec.md and no architecture.md in this folder. Product work stays in justinyurasits/design | True for this change. No further date is stated |
| A reader can see that nothing is validated yet | [README.md](README.md) says what is written, what is built, and what is validated, and does not claim a validation that has not happened | The README in this change says the collection is not validated |
| The public record stays free of personal and client data | `python tools/validate.py` reports no email address and no obvious secret marker. Client names are checked in review. The validator does not detect client names | Exit 0 on the pull request, and no client names in the files Justin merges |

This project has no product spec. Each later component's brief and spec trace to this brief.

## 5. The wedge

Justin-os is case study #1. It is the first case study named for this collection. It is not added in this change.

## 6. Out of scope, on purpose

- A build repository comes later. This change does not create one.
- Personal and client data stay out of this public repository.
- Product work stays in justinyurasits/design.
- The justin-os component and morning-brief-prompt.md are a later change, not this folder.

## Open

- A scene for the painful moment, with a cost in time or money, is not stated. Justin decides whether to add one.
- A prior tool or habit this collection replaces, beyond the split from justinyurasits/design, is not named. Justin decides whether to name one.
- Numeric targets and dates for the goals are not stated. Justin decides them.
