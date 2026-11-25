---
type: prompt
status: draft
---

# Project name — Component name <Name> Prompt

*Optional. One file per prompt the component sends to a model; name it
`<name>-prompt.md`. This is the reviewed design of the prompt. When a code repository
exists, it holds the copy that runs, and a test there checks the two match. Until then,
say where the running copy lives, for example a scheduled routine. A change to that
copy is a new row in the version log, in the same working session. The assistant
proposes it by pull request.*

## What it's for

*The decision or output the model produces with this prompt, and what code does with it.*

## The prompt

```text
<the full prompt, exactly as the running copy sends it>
```

## Version log

| Version | Date | Change | Why |
| --- | --- | --- | --- |
| *1* | *YYYY-MM-DD* | *First version* | *<reason>* |
