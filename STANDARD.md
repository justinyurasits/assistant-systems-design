---
type: standard
status: current
---

# Assistant Systems Design — Document Standard

Nov 24, 2026 · @Justin

The document model for the `assistant-systems-design` repository. It forks [`justinyurasits/design` STANDARD.md](https://github.com/justinyurasits/design/blob/3d9b641237a3926149ad00c94f6343ce8b8e1a66/STANDARD.md) revision 61 (`3d9b641`). This file is the source. The assistant drafts a change in a pull request, the owner reviews and merges, and the merged file on `main` is what everyone reads. A change in the upstream `design` repository is adopted only on purpose, in a pull request that names what was taken and why. Nothing in this repository is synced from another document.

Repo operation rules stay in `AGENTS.md`: no direct commits to `main`, the owner merges, no history rewrites, no secrets, and no personal or client data. Those are guardrails against damage. This document holds the model, which is the part that grows.

## Component structure

Every component has the same files from the day it is created. A file with nothing settled in it yet exists at `status: draft` and says what is open. Nothing holds two jobs.

| File | Its one job |
| --- | --- |
| `README.md` | Index, plus the short public version: what this is, why it exists, the two or three decisions worth knowing, and what is designed vs. built vs. validated |
| `brief.md` | Who it's for, the painful moment, what it replaces, what's out of scope. Never requirements, decisions or design; those have their own files |
| `spec.md` | What it must do. The domain, named and bounded, and the requirements that check it. A requirement cites the capability ID it serves when the project has a product spec. A pointer if the domain lives elsewhere |
| `design.md` | Architecture, boundaries, and the decision log |
| `plan.md` | Work still ahead: milestones, each with an exit criterion. Finished work moves to the build log; bugs and small tasks are GitHub issues |
| `build-log.md` | What happened, in order, and what each finding changed. An entry uses the pull request's Did / Broke / Learned labels |
| `images/` | Static exports, re-exported when the drawing changes |

**Optional, by named type** — any number per component, and only these two:

| File | Its one job |
| --- | --- |
| `<slice>-design.md` | Technical design for one vertical slice |
| `<name>-prompt.md` | A prompt the component sends to a model, with its version log. The code repository holds the copy that runs, and a test there checks the two match |

A new optional type is added to this table when a real document needs one, so every document has a name and a stated job. A file that fits no row is a reason to add a row, not to keep an unnamed file.

## Rules

- **One decision, one source.** Decisions live in that component's `design.md` log. Product-level decisions, which span components, live in the project's `architecture.md` decision log. A plan or build log may reference a decision; neither records one.
- **One document, one job.** If a file matches two rows above, it is two files.
- **Front matter: `type` and `status`** (`draft | current | superseded`) on every design document in this repository, written in the file. `type` and `status` do not live anywhere else. A README's `type` is `readme`. This file's `type` is `standard`.
- Filenames are lowercase-kebab `.md`. No version numbers in filenames.
- **Repo-authored.** Every document is written in this repository by pull request. The assistant drafts; the owner reviews and merges. The merged file on `main` is the source. A placeholder stays a placeholder until a pull request fills it.
- **Titles** follow `<Project> — <Component> <doc type>`, with the doc type taken from the file name: "Construction OS — Corpus Design", "Construction OS — Intake Router Classifier Prompt". Project-level docs drop the component ("Construction OS — Brief"). Docs for this repository itself use "Assistant Systems Design" as the project ("Assistant Systems Design — Document Standard"). The doc's top heading matches that title. A README is the exception: its top heading is the project name, the component name, or the repository name.
- Restructuring happens in a pull request in this repository. The merged file on `main` is what the next change starts from.
- A new component is this file set, not a decision about which files to make.
- **This repository is public.** Documents hold methods and decisions. They do not hold email addresses, secrets, or client names.

## Project structure

A project is a folder under the repo root holding one product's documents, or a collection of independent builds, with its components as subfolders beneath it.

**Required at the project level:** `README.md`, `brief.md`.

**Optional, by named type:**

| File | Its one job |
| --- | --- |
| `principles.md` | Craft knowledge — what building this taught, each principle anchored to the incident that taught it and to where it is enforced |
| `product-spec.md` | What the product must do for its users, independent of implementation: capabilities, each with a stable ID in its heading (`<PROJECT>-CAP-<nn>`) and acceptance criteria; user journeys, including incomplete input and failures; and product-wide requirements. Needed once a project's components make up one product. A project that groups independent builds, such as a set of case studies, has no product spec or architecture: its brief says what's in the folder and why it's grouped, and each component's own brief and spec say what it must do. A capability moves to its own spec when it is big enough to manage on its own: several journeys, complicated rules, or its own acceptance-test suite |
| `architecture.md` | How the components fit together and how a request moves through them. Product-level decisions live in its decision log |

The project level is deliberately not a fixed file set the way a component is, and the difference is structural rather than a matter of judgment. Components repeat: each does the same job, so fixing the set removes decisions that would otherwise get made differently each time. Projects do not repeat. A project whose components make up one product, and which has more than one of them, needs an architecture document. A single-component product does not, and neither does a project that groups independent builds. New optional types are added to the table above as they appear, so a document has a name and a stated job rather than arriving ad hoc.

A new project gets a folder, a README, a brief, and a row in the root README's index table.

## The reference project

`_template/` at the repo root is this standard as files, in three folders. `project/` holds every required and optional project-level file; `component/` holds the full component set; `repo/` holds the files every code repository starts with. A README at `_template/` says which to copy where, and the README in each of those three folders repeats its own destination. Each file says what belongs in it. To start a project, copy `project/` and rename it; to add a component, copy `component/` into the project; to start a code repository, copy `repo/` into it. Real projects keep their product-level docs at the top of their folder; the `project/` subfolder exists only in the template, to keep it apart from the components.

The template shows the standard; it adds nothing to it. Where the two differ, this document wins and the template is fixed in the same pull request. `_template/` is repo-authored, edited by pull request like every other file here. Instructional placeholders — lines in italics, and `<angle brackets>` — belong only in `_template/`.

## Repositories

Every repository a project here describes follows the same conventions, so a person or an assistant can find its way around any of them.

- **Naming.** A product built across several repositories names them `<product>-<part>`: `construction-os-corpus`, `construction-os-workbench`. A product in one repository takes its plain name.
- **Starting files.** Every code repository starts from `_template/repo/`: `AGENTS.md`, a pull request template, `README.md`, `.gitignore`, and `.env.example` when it uses secrets.
- **AGENTS.md.** The standard sections are copied from `_template/repo/AGENTS.md` and marked with the template version they came from, so drift shows. One section is the repository's own: its layout, conventions and domain language. A repository may override a standard rule only by saying so in that section, with the reason.
- **README.** What it is, its status (`active`, `prototype` or `archived`), how to run it, and a link to its design folder here.
- **Sidebar.** A one-line description and topics on GitHub.
- **Links both ways.** A code repository links to its design folder; the design folder's README links to the code.

## How design and code work together

Every project works the same way.

- **Every design doc lives here.** No project keeps design docs in its code repository. The one exception is visual design: colors, type, marks and components live in the brand-system repository, with their own rules and change control. Files generated from code, such as a page built from recorded runs, stay with the code.
- **Design leads, code follows.** A change to what the product does, to a requirement or to the architecture is made in the design docs first, and the code pull request cites it. Code pull requests never edit design docs. When the work needs a design change, stop and propose it. Once the owner approves, the assistant drafts it in a pull request here. The code pull request follows and cites it.
- **The issue is the plan.** An approved GitHub issue authorizes the work; the spec and design constrain how it is done. If they conflict, or the work needs a change the design doesn't cover, stop and say so.
- **Pull requests capture the small stuff.** Decisions made while coding and what the work taught go in the pull request under the template's *Decisions (proposed)* and *Build notes* headings. Merging the pull request approves its decisions. That covers implementation choices made inside an approved issue only. A decision that changes a requirement, the architecture, a security boundary or documented behavior is a design change: it goes through the design docs first (Design leads, code follows), and a code pull request can't approve it.
- **Roll-up.** The assistant asks "Roll up to design?" when a pull request the assistant opened is merged, when an issue or milestone is done, and at the end of a working session with the owner if unrecorded decisions exist. On yes, the assistant gathers Decisions and Build notes from pull requests merged since the last roll-up and proposes them in a pull request in this repository: decisions for the component's `design.md` log, findings for `build-log.md`, and lessons that generalize beyond the work (what the next component or project would want to know) for the project's `principles.md`, under the principle they serve or flagged as a candidate new one. On no, the assistant does not ask again until the next trigger. Nothing enters the record until the owner approves that pull request. The build log notes each roll-up ("Roll-up: `<repo>` #`<first>`–#`<last>`"), which marks where the next one starts.
- **Tests can read design docs.** A code repository's tests may read its design docs to check the code against them. Those files are then part of the contract: their headings and formats stay stable, so renaming a heading or reshaping a table needs a matching code pull request.
- **Finding the design repo.** `../assistant-systems-design` means next to the repository's main checkout. A session working in a git worktree finds it from the main checkout, or from a `DESIGN_DIR` override, not from the worktree's own folder.

## Maintaining this document

**Changes are made in this file.** A pull request edits it, the owner merges, and the merged file on `main` is the source.

**This document forks `justinyurasits/design` STANDARD.md revision 61.** Upstream changes are adopted only on purpose. A pull request that adopts one says what was taken and why. Nothing watches the upstream file, and nothing copies it on a schedule.

**Every change gets a dated line in the history below.** One line, what changed and why. This is what makes a convention trustworthy to someone reading it six months later, including an assistant that has never seen the conversation it came from.

**The structure is checked automatically.** `tools/validate.py` checks every project and component against this standard: required files, front matter `type` and `status`, the title pattern, named types, README sections against `_template/`, relative links, and that the root README links every project folder. It runs on every pull request, and an error fails the check. The script lands with the repository tooling. A pull request that changes the document shape updates the script in the same pull request. `_template/` is skipped for link and placeholder checks: its links are written for where copies end up, and its italics and angle brackets are the instructions.

**A component that doesn't fit is evidence about the standard, not an exception to it.** Either the shape is wrong and this document changes, or the component is wrong and it changes. No component is exempted. Exemptions are how a convention stops being one.

## Change history

| Date | Change |
| --- | --- |
| 2026-11-25 | Role names in the generic rules: the assistant drafts, the coding agent opens pull requests, and the owner approves and merges. Roll-up triggers match `AGENTS.md`: a merged pull request, a finished issue or milestone, and the end of a working session with the owner if decisions are still unrecorded. The ten-turn trigger is dropped. On no, do not ask again until the next trigger. |
| 2026-11-24 | Forked from `justinyurasits/design` STANDARD.md revision 61 and adapted for this repository. Dropped the external-doc sync layer: `sync-manifest.yaml`, `DOCS.md`, `tools/build_docs.py`, and the sync header. Renamed the design checkout path from `../design` to `../assistant-systems-design`, and the code-repo operating-rules file from `CLAUDE.md` to `AGENTS.md`. `type` and `status` live in each file's front matter. Documents are written here by pull request; the assistant drafts and the owner merges. Roll-up is a pull request in this repository. A build-log entry uses the pull request's Did / Broke / Learned labels. Upstream changes are adopted only on purpose. The reasons for the rules kept from revision 61 are in that revision's change history. |
