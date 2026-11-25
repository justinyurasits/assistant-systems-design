# <repo-name>

<!-- standard: assistant-systems-design/_template/repo/AGENTS.md v1
     Adapted from justinyurasits/design _template/repo operating rules v1.7
     (STANDARD.md revision 61). Upstream changes are adopted only on purpose.
     Sections 1–6 are the standard: copy them unchanged, filling in only the <angle brackets>.
     Section 7 is this repository's own. To change a standard rule here, say so under
     "Overrides" in section 7, with the reason.
     Roles and roll-up triggers match assistant-systems-design/AGENTS.md.
     Do not copy a person's name into this file. -->

## Roles

These rules bind both the assistant and the coding agent.

- **The assistant** scopes work, drafts issues and specs, briefs the coding agent, and runs the roll-up conversation with the owner.
- **The coding agent** makes the commits, the branch, and the pull request for an approved issue. One job at a time. Not a standing bot.
- **The owner** approves issues, reviews and merges, and is the only one who approves a record.

Draft-only sends bind the assistant. Branch and pull-request rules bind the coding agent.

## 1. What this is

*One or two sentences: what this repository holds, for which product.*
Status: *active · prototype · archived*.

## 2. Design

The design docs for this repository are in the `assistant-systems-design` repository,
cloned next to this one, at `../assistant-systems-design/<project>/<component>/`. Pull
it before planning. In a git worktree, `../assistant-systems-design` means next to the
main checkout, not next to the worktree. A `DESIGN_DIR` override, when set, wins over
that path.

Before proposing work, read in this order (skip any the project doesn't have yet):

1. `../assistant-systems-design/<project>/brief.md`: why it exists and for whom
2. `../assistant-systems-design/<project>/product-spec.md`: what the product must do, by capability ID
3. `../assistant-systems-design/<project>/architecture.md` and `principles.md`: how the parts fit, and
   the rules every design decision follows
4. `../assistant-systems-design/<project>/<component>/brief.md` and `spec.md`: who this component is for,
   and what it must do
5. `../assistant-systems-design/<project>/<component>/design.md`: how it works, and the decision log
6. `../assistant-systems-design/<project>/<component>/<slice>-design.md`: the build design for the slice
   the issue belongs to
7. `../assistant-systems-design/<project>/<component>/plan.md`: the milestones still ahead

- **Design leads, code follows.** If the work needs a change to what the product does,
  to a requirement or to the architecture, stop and propose the change.   Once the owner
  approves it, make it in a pull request in `assistant-systems-design`, and build
  against it after it's merged. Never put a design change in this repository's pull
  request, and don't build ahead of the design.
- **Working in `../assistant-systems-design`.** Before changing anything there (a design
  pull request or a roll-up), read `../assistant-systems-design/AGENTS.md` and
  `../assistant-systems-design/STANDARD.md` and follow them.
- **When the design is silent, ask.** Don't improvise behavior, copy or scope.
- **When the design and this repository disagree, say so.** Don't guess which is right.

## 3. How work happens

- **The issue is the plan.** Work only from a GitHub issue, and read it first
  (`gh issue view <N>`). The issue authorizes the work; the spec and design constrain
  how it's done. If they conflict, stop and say so. With no issue, write the work up as
  a proposed issue and wait.
- One issue, one branch, one pull request. Branch name: `issue-<N>-<short-description>`.
- Anything outside the issue gets a new issue. Don't widen the scope.
- Never commit to `main`. Never merge: the owner reviews and merges. This binds the coding agent.

## 4. Checks

- Run the checks listed in section 7 before opening a pull request, and paste the
  results into it.
- A failure is never ignored. Either the change is wrong or the check is; say which.
- Never change an expected result to make a check pass. Report the mismatch and stop.

## 5. Every pull request

Fill in `.github/pull_request_template.md`:

- `Closes #<N>`, and what changed and why, in plain English.
- How each acceptance criterion in the issue was checked.
- **Decisions (proposed):** choices made while coding: the decision, the options, why,
  and what would change it. Merging the pull request approves them. That covers
  implementation choices inside the issue only. A decision that changes a requirement,
  the architecture, a security boundary or documented behavior is a design change
  (section 2): stop and propose it instead.
- **Build notes:** what you did, what broke, what it taught (Did / Broke / Learned).

## 6. Roll-up, ask before, never

**Roll-up.** Ask "Roll up to design?" when a pull request you opened is merged, when an
issue or milestone is done, and at the end of a working session with the owner if
unrecorded decisions exist.

- On yes: collect Decisions and Build notes from pull requests merged since the last
  roll-up (the latest "Roll-up:" line in the component's `build-log.md`). Open a pull
  request in `assistant-systems-design` that proposes decisions for the `design.md`
  decision log and findings for `build-log.md`, ending with the line
  `Roll-up: <repo> #<first>–#<last>`. Also propose any lesson that generalizes beyond
  this work for the project's `principles.md`, under the principle it serves or flagged
  as a candidate new one.
- On no: don't ask again until the next trigger.
- Nothing enters the design record until the owner approves that pull request.

**Ask before:**

- adding a dependency
- changing a prompt, tool description, rubric, or anything else that changes what a
  model decides
- anything not in the issue

**Never:**

- read, print or edit `.env`. Secrets live only there; `.env.example` holds key names only
- commit secrets, API keys, email addresses, personal data, or client names. The design
  repository is public
- rewrite git history

## 7. This repository

*The only section that differs between repositories.*

- **Layout:** *what each top-level folder holds. README.md describes the same folders
  for people; when a folder is added, moved or retired, update both.*
- **Run:** *the commands to run it locally.*
- **Checks:** *the test command and any validators every pull request runs.*
- **Conventions:** *language and version, code style, domain language.*
- **Overrides:** *a standard rule this repository changes, the replacement, and why.
  "None" if none.* The design repository's own `AGENTS.md` says none currently. A build
  repository started from this folder writes its exceptions here.
