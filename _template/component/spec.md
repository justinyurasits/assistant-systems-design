---
type: spec
status: draft
---

# Project name — Component name Spec

*What the component must do, and how anyone can check that it does. Behavior, not
implementation. If the domain is defined elsewhere (a corpus, a standard), point to it
instead of copying it.*

## The domain

*The things this component deals with, named and bounded. Where each one's rules are
defined.*

## Requirements

### *<Requirement name>*

*What the system must do, in one or two sentences.*

**Serves:** *the capability it delivers, by ID. When the project has a product spec:
[PRJ-CAP-01](../product-spec.md#prj-cap-01-capability-name). When the project groups
independent builds and has no product spec, name the component requirement this
serves instead of linking a capability that does not exist.*

**Acceptance criteria**
- *Given <situation>, when <action>, then <observable result>.*
- *A failure case: what it must refuse or flag.*

*Each requirement gets a heading, so a plan, an issue or a test can link straight to it.*

## Boundaries

- **Not in the domain:** *what this component never touches.*

## Known gaps

- *What's undecided or missing in the source, and who decides it.*
