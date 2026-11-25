---
type: spec
status: draft
---

# Assistant Systems — Justin-os Spec

What justin-os must do, and how to tell that it did. Behavior Justin can observe. No collection capability ID is defined in [../brief.md](../brief.md), so each requirement below is a component requirement.

## The domain

People and helpers: Justin, Sandra, Product Lead, and the one-job build crew (architect, designer, coder).

Connected sources, read by default: GitHub through the Cursor GitHub app, two Gmail accounts, two Google Calendar accounts, and Google Drive. Private account names are not part of this spec.

Kept in the shared workspace on Sandra's computer, under justin-os/: README, tasks, conversations/log, notes/, products/, and clients/. The clients/ folder is where client material lives for the assistants. Client names are not copied into this repository. A Command Center page is refreshed by the morning brief.

## Requirements

### Standing assistants and one-job agents

Sandra and Product Lead are standing assistants. Architect, designer, and coder each run as a cloud agent for one job, then stop. Serves component requirement JOS-ROLE-1.

**Acceptance criteria**

- Given a helper in this system, when someone reads [design.md](design.md), then the helper is named as a standing assistant or as a one-job cloud agent, and the design says where Justin can see it.
- Given the architect or the coder, when Justin looks for a standing-bot icon and finds none, then the design already says that helper is an ephemeral cloud agent.

**Failure case:** a helper is added with no kind, or with no place Justin can see it. The design is not ready to merge until both are stated.

### Connectors report failure and do not write

A routine may read GitHub, Gmail, Google Calendar, and Google Drive. It does not send, label, archive, trash, or edit those sources unless Justin has approved that write outside the read-only brief. Serves component requirement JOS-CONN-1.

**Acceptance criteria**

- Given a connector error or a missing permission, when the run continues, then the brief says so in one line and does not invent the missing events or mail.
- Given both calendars, when one connection lacks a permission, then that connection's gap is the one line, and the other connection is still read.

**Failure case:** a connector is down. The run reports the failure. It does not present an empty day as if the calendar had been read.

### A send stays a draft

Nothing is sent, posted, or delivered on Justin's behalf without his approval. Serves component requirement JOS-CONN-2.

**Acceptance criteria**

- Given a request to send mail or a message, when Justin has not approved that send, then the assistant drafts it and stops.

**Failure case:** a send is requested during the morning brief or any other read. The send is not performed. The brief stays read-only.

### The weekday morning brief

On weekdays, at 8:00 AM America/New_York, plus or minus 15 minutes, Sandra delivers a short brief in chat. The text of the routine is [morning-brief-prompt.md](morning-brief-prompt.md) version 1. Serves component requirement JOS-ROUTINE-1.

**Acceptance criteria**

- Given a weekday run, when the brief is delivered, then it covers today's and tomorrow's events in ET, business mail that needs a reply or action, a short personal-mail section, a noise count, and the GitHub items the prompt names.
- Given mail in both Gmail accounts, when the brief is built, then duplicates across the two inboxes are dropped, and a thread Justin already answered is not flagged.
- Given newsletters, promos, receipts, security alerts, digests, and GitHub notification mail, when the brief is built, then those are counted as noise and not listed one by one.

**Failure case:** the run is asked to label, archive, trash, or send mail while building the brief. It does not. The same failure applies to changing a calendar event or a GitHub item.

### The workspace follows the source

Tasks and the conversation log are updated from what the sources show. Serves component requirement JOS-MEM-1.

**Acceptance criteria**

- Given tasks.md, when the brief updates it, then a task is marked done only when the source shows it done.
- Given the run, when it writes the log, then it adds one line to conversations/log.md and refreshes the Command Center page in place.

**Failure case:** a task would be marked done with nothing in the source showing it done. The update is not made.

## Boundaries

- Not in the domain: account addresses, client names, the contents of personal mail, and job-search details.
- Not in this repository: the build repository, and any second assistant system.

## Known gaps

- One calendar connection still needs one more permission. The permission's name is not recorded. Justin decides and grants it. Until then JOS-CONN-1's one-line failure report is the required behavior.
- Version 1 of the morning-brief prompt still describes the website pilot as current work. The pilot was paused. Whether version 2 changes that sentence is open. Justin decides.
- The success measures in [plan.md](plan.md) are not confirmed. Justin decides them. This spec does not treat them as acceptance tests yet.
