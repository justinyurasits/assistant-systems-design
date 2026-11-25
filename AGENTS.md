# AGENTS.md

Operating rules for this repository. It is public. Documents hold methods and decisions, not email addresses, secrets, or personal or client data.

Justin is the owner of this repository. The document model is in [STANDARD.md](STANDARD.md). These rules are the guardrails. That file is the model. Where they differ, the standard is right.

## Who the rules apply to

Every rule in this file binds both the assistant and the coding agent.

- **The assistant** is the chief-of-staff assistant. The assistant scopes work, drafts issues and specs, briefs the coding agent, and runs the roll-up conversation with the owner.
- **The coding agent** is a Cursor cloud agent, one job at a time, not a standing bot. The coding agent makes the commits, the branch, and the pull request for an approved issue.
- **The owner** approves issues, reviews and merges, and is the only one who approves records.

Draft-only sends bind the assistant. Branch and pull-request rules bind the coding agent.

## 1. What this is

Design documents for assistant systems, one folder per project. No project keeps its design docs in a code repository. A new code repository, when one exists, starts from `_template/repo/` and reads the design from here.

## 2. Design leads

Read `STANDARD.md` before creating or restructuring a document.

- **Design leads.** A change to what a system does, to a requirement, or to the architecture is made in the design docs first.
- **When the design is silent, ask.** Don't improvise behavior, copy, or scope.
- **When the design and a future code repository disagree, say so.** Don't guess which is right.
- A new project starts as a copy of `_template/project/` and gets a row in the root README. A new component starts as a copy of `_template/component/`.

## 3. How work happens

- **The issue is the plan.** Work only from an approved GitHub issue, and read it first (`gh issue view <N>`). GitHub is read-only except on an approved issue and its branch. With no approved issue, do not change the repository.
- One issue, one branch, one pull request. Branch name: `issue-<N>-<short-description>`. This binds the coding agent.
- Never commit or push to `main`. Never merge: the owner reviews and merges.
- Anything outside the issue gets a new issue. Don't widen the scope.
- **Draft-only sends.** This binds the assistant. Draft the message and stop. Nothing is sent, posted, or delivered without the owner's approval.

## 4. Checks

- Run `python tools/validate.py` from the repo root before opening a pull request. It checks the structure against `STANDARD.md`. CI runs the same check on every pull request. An ERROR fails the check.
- A failure is never ignored. Either the change is wrong or the check is; say which.
- Never rewrite an expected result to make a check pass. Report the mismatch and stop.

## 5. Every pull request

Fill in `.github/pull_request_template.md`:

- `Closes #<N>`, and what changed and why.
- How each acceptance criterion was checked.
- **Decisions (proposed):** the decision, the options, why, and what would change it. Merging approves implementation choices inside the issue only. A decision that changes a requirement, the architecture, a security boundary, or documented behavior is a design change and is recorded in the design docs.
- **Build notes:** Did, Broke, Learned.

## 6. Roll-up, ask before, never

**Roll-up.** Ask "Roll up to design?" when a pull request you opened is merged, when an issue or milestone is done, and at the end of a working session with the owner if unrecorded decisions exist.

- On yes: open a pull request in this repository that proposes decisions for the component's `design.md` log, findings for `build-log.md`, and lessons that generalize for the project's `principles.md`. End that proposal with the line `Roll-up: assistant-systems-design #<first>–#<last>`.
- On no: don't ask again until the next trigger.
- Nothing enters the record until the owner approves it.

**Ask before:**

- changing a prompt, tool description, rubric, or anything else that changes what a model decides
- anything not in the issue

**Never:**

- commit or push to `main`, or merge
- commit secrets, email addresses, personal data, or client names
- rewrite git history
- send, post, or deliver anything that was only drafted

## 7. Overrides

Repo-specific exceptions go here, with the reason. None currently.

A future build repository started from `_template/repo/` records its own exceptions in that copy's section 7.
