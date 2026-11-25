---
type: readme
status: current
---

# Assistant Systems Design

Design documents for assistant and agentic systems. This repository is public. It holds methods and decisions, not personal or client data.

## How these docs are written

The assistant drafts a change in a pull request. The owner reviews and merges. The merged file on `main` is the source. Documents are written here, not synced from Claude Docs. Where this README and [STANDARD.md](STANDARD.md) differ, the standard is right.

## Files

| File | What it is |
| --- | --- |
| [STANDARD.md](STANDARD.md) | The document model: the file set, front matter, titles, and how design and code work together. |
| [AGENTS.md](AGENTS.md) | Operating rules. Justin merges. GitHub is read-only except on an approved issue and its branch. |
| [_template/](_template/) | The standard as files. Copy a folder from here to start a project, a component, or a code repository. |
| [tools/validate.py](tools/validate.py) | Checks the tree against the standard. Run `python tools/validate.py` from the repo root. |

## Adding a project or a component

Copy `_template/project/` to a new folder at the repo root, then add a row for that folder in the Projects table. The link target is the project folder. Copy `_template/component/` into the project to add a component. Fill the copied files in a pull request. Instructional placeholders stay in `_template/`. A live project does not keep them.

## Projects

| Project | What it is |
| --- | --- |
| [systems](systems/) | A collection of independent assistant-system case studies. |
