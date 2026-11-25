---
type: readme
status: draft
---

# Component name

*Copy `component/` to `<project-name>/<component-name>/`. Replace every italic line
and `<angle bracket>`.*

*One or two sentences: the job this component owns within the project, and its first
slice.*

Product-level docs are one folder up, in [../](../).

## Where things stand

*Two or three sentences: what is designed, what is built, what is validated, with the
evidence. Say plainly what isn't running yet.*

**Code:** *[`<product>-<part>`](https://github.com/justinyurasits/<product>-<part>) — its
AGENTS.md points back to this folder. Omit this line until a code repository exists.*

## The docs

| File | What it is |
| --- | --- |
| [brief.md](brief.md) | This component's customer, painful moment and scope, where they narrow the product brief. |
| [spec.md](spec.md) | What it must do: requirements, each with acceptance criteria, citing a capability ID when the project has one. |
| [design.md](design.md) | How it works, its boundaries, and the decision log. Decisions are recorded once, here. |
| [slice-design.md](slice-design.md) | Optional. Build design for one vertical slice. One file per slice, named `<slice>-design.md`. |
| [name-prompt.md](name-prompt.md) | Optional. A prompt the component sends to a model, with its version log. One file per prompt, named `<name>-prompt.md`. |
| [plan.md](plan.md) | Milestones still ahead, each with its exit criterion. Work only. |
| [build-log.md](build-log.md) | What happened, in order, and what each finding changed. Did, Broke, Learned. |

## How these docs work

Files are written in this repo by pull request. The assistant drafts. The owner reviews and
merges. The merged file on `main` is the source. `type` and `status` live in each
file's front matter.
