---
type: design
status: current
---

# Assistant Systems — Justin-os Design

How the parts work, and the decisions Justin approved on 2026-11-24. The system is not validated.

## 1. Scope and boundaries

| In scope now | Deferred |
| --- | --- |
| Sandra as the standing chief-of-staff assistant | The five-weekday brief streak |
| Product Lead as the second standing assistant | The remaining calendar permission |
| Architect, designer, and coder as one-job cloud agents | Role prompts for the build crew |
| The shared workspace and the Command Center page | The build repository |
| The read-only weekday morning brief | A second assistant system, not chosen |
| This public design record | Product work and the website pilot, paused |

## 2. How it works

Sandra is a standing assistant. She keeps notes, tasks, and a conversation log in the shared workspace, runs the weekday morning brief at about 8:00 AM ET, and drafts documents in this repository by pull request.

Product Lead is a second standing assistant. The role holds per-product and per-client vision. Client names are not in this repository.

The build crew is architect, designer, and coder. Each is a Cursor cloud agent started for one job. They are not standing bots. The architect does not show a standing-bot icon in the left panel. The coder is reached on cursor.com.

The shared workspace is on Sandra's computer, at justin-os/. It holds README, tasks, conversations/log, notes/, products/, and clients/. The morning brief refreshes a Command Center page in place.

Connectors, read by default: GitHub through the Cursor GitHub app, two Gmail accounts, two Google Calendar accounts, and Google Drive. One calendar connection still needs one more permission. Addresses are not recorded here.

The brief's steps are specified in [morning-brief-prompt.md](morning-brief-prompt.md). It reads the workspace, both calendars, and both inboxes, separates business mail from a short personal section, counts noise, reads GitHub, updates tasks only from the source, and sends the brief in chat.

## 3. Constraints

- The morning brief is read-only. It does not send, draft, label, archive, trash, or change mail, calendar events, or GitHub items.
- Any other send stays a draft until Justin approves it.
- GitHub is read-only for assistants except an approved issue and its branch. One issue, one branch, one pull request. Justin merges.
- This repository is public. No secrets, no account addresses, no client names, no job-search details.
- Design leads. A change to what the system does is made in these documents first.

## 4. Decision log

One entry per decision. Same day, so the list follows the order they apply to this system, with the inherited standard last. A plan or build log may point here. Neither records a new decision.

| Date | Decision | Options considered | Why | What would change it |
| --- | --- | --- | --- | --- |
| 2026-11-24, 5:13 PM ET | Products and the website pilot are paused. The practice of building assistant systems is the focus. | Continue the pilot and product work, or pause both. | Justin approved the pause in chat at that time. | Justin says the pilot or product work resumes. |
| 2026-11-24 | Assistant systems have their own public design repository, assistant-systems-design, instead of a folder in justinyurasits/design. A build repository comes later. | A folder in the design repo, which was getting cluttered, or this separate public repo, mirroring the two-repo product setup. | Justin approved the split. The build repo waits until there is running config worth versioning. | Justin moves the case studies back, or starts the build repo. |
| 2026-11-24 | Documents are written in this repo by pull request. Sandra drafts and Justin merges. AGENTS.md is the operating-rules file. STANDARD.md forks design revision 61. | Sync from Claude chat, or pull requests here. | Justin approved repo-authored documents. The sync layer is not part of the fork. | Justin chooses a different authoring path. That would be a change to STANDARD.md. |
| 2026-11-24 | GitHub is read-only for assistants except approved build steps. One issue, one branch, one pull request. Justin does all merging. | Assistants merge and edit outside an approved issue, or they stay inside that rule. | Justin approved it in chat. | Justin changes who may merge or what GitHub writes are allowed. |
| 2026-11-24 | Nothing is sent without Justin's approval. Sends stay drafts. | Send on the assistant's judgment, or draft only. | Justin approved drafts only. | Justin approves a class of sends. Until then, none go out. |
| 2026-11-24 | The morning brief is strictly read-only. | A brief that can also file or send, or a brief that only reads. | Justin approved the read-only brief. | Justin changes the routine. That is a new prompt version. |
| 2026-11-24 | Personal mail has its own short section at the bottom of the brief, separate from business mail. | One mixed list, or business mail above a short personal section. | Most of the real inbox volume was not business mail. The section follows that, instead of a plan that treated business mail as the bulk. | Justin changes how the brief is sectioned. |
| 2026-11-24 | Design leads and code follows. Inherited from Justin's design standard. | Not a new choice this day. | The standard already said it. This system adopts it. | A merged change to STANDARD.md. |
