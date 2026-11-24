# AGENTS.md

Operating rules for this repository. It is public. Documents hold methods and decisions, not email addresses, secrets, or personal or client data.

Sandra drafts. Justin reviews and merges. The document model is in [STANDARD.md](STANDARD.md). These rules are the guardrails. That file is the model. Where they differ, the standard is right.

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
- One issue, one branch, one pull request. Branch name: `issue-<N>-<short-description>`.
- Never commit or push to `main`. Never merge: Justin reviews and merges.
- Anything outside the issue gets a new issue. Don't widen the scope.
- **Draft-only sends.** Draft the message and stop. Nothing is sent, posted, or delivered without Justin's approval.

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

**Roll-up.** Ask "Roll up to design?" when a pull request you opened is merged, when an issue or milestone is done, and about every ten turns of work since you last asked.

- On yes: open a pull request in this repository that proposes decisions for the component's `design.md` log, findings for `build-log.md`, and lessons that generalize for the project's `principles.md`. End that proposal with the line `Roll-up: assistant-systems-design #<first>–#<last>`.
- On no: don't ask again for another ten turns.
- Nothing enters the record until Justin approves it.

**Ask before:**

- changing a prompt, tool description, rubric, or anything else that changes what a model decides
- anything not in the issue

**Never:**

- commit or push to `main`, or merge
- commit secrets, email addresses, personal data, or client names
- rewrite git history
- send, post, or deliver anything that was only drafted
