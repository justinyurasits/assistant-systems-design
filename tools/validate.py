#!/usr/bin/env python3
"""Structural checks for assistant-systems-design, against STANDARD.md.

Run from the repo root:  python tools/validate.py
Exit code 1 if any ERROR is found. WARNINGs are reported and do not fail the run.
Zero project folders is valid.

What it checks
  - every project folder has README.md and brief.md
  - every component folder has the full component file set, including images/
  - repo-authored .md files in those folders have front matter type and status
  - a non-README top heading uses the title pattern (an em dash)
  - a project or component README has the sections in the matching _template README
  - a markdown file that is not a required or named optional type is a WARNING
  - relative links resolve ( _template/ is skipped: its links are for copies )
  - the root README links every project folder
  - no file carries a "Synced from Claude Docs" header
  - no text file contains an email address or an obvious secret marker

Not checked: sync manifests, a generated doc index, or a doc-build script.
Those are not part of this repository.
"""

import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", ".github", "tools", "_template"}
STATUSES = {"draft", "current", "superseded"}
PROJECT_REQUIRED = ["README.md", "brief.md"]
COMPONENT_REQUIRED = [
    "README.md",
    "brief.md",
    "spec.md",
    "design.md",
    "plan.md",
    "build-log.md",
    "images",
]
PROJECT_OPTIONAL = {"principles.md", "architecture.md", "product-spec.md"}
COMPONENT_OPTIONAL_RE = re.compile(r"^[a-z0-9-]+-(design|prompt)\.md$")
SYNC_HEADER = re.compile(r"^> \*\*Synced from Claude Docs", re.M)
LINK = re.compile(r"\]\(([^)\s]+)\)")
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
SECRET_MARKERS = [
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}"),
    re.compile(r"\bsk-(?:ant-|proj-)?[A-Za-z0-9_-]{20,}\b"),
    re.compile(
        r"(?i)\b(?:api[_-]?key|secret|password|token|aws_secret_access_key)\b"
        r"\s*[:=]\s*['\"]?[A-Za-z0-9/+_.=-]{8,}"
    ),
]
SKIP_SCAN_EXT = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf", ".gz", ".zip", ".woff", ".woff2",
}

errors, warnings = [], []


def err(path, msg):
    errors.append(f"ERROR   {path}: {msg}")


def warn(path, msg):
    warnings.append(f"WARNING {path}: {msg}")


def rel(path):
    return os.path.relpath(path, ROOT)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def read_text(path):
    """Return text, or None for a binary file or a file that is not UTF-8."""
    ext = os.path.splitext(path)[1].lower()
    if ext in SKIP_SCAN_EXT:
        return None
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except (UnicodeDecodeError, OSError):
        return None


def front_matter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    try:
        return yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError:
        return False


def top_heading(text):
    # The heading is the first H1 after front matter, so a rule in the body
    # is not mistaken for the title.
    body = text
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            body = text[end + 4:]
    match = re.search(r"^# (.+)$", body, re.M)
    return match.group(1).strip() if match else None


def check_markdown(folder):
    for name in sorted(os.listdir(folder)):
        path = os.path.join(folder, name)
        if not name.endswith(".md") or not os.path.isfile(path):
            continue
        text = read(path)
        fm = front_matter(text)
        if fm is None:
            err(rel(path), "repo-authored file without front matter (type, status)")
        elif fm is False:
            err(rel(path), "front matter is not valid YAML")
        else:
            if not fm.get("type"):
                err(rel(path), "front matter has no type")
            if fm.get("status") not in STATUSES:
                err(rel(path), f"front matter status {fm.get('status')!r}; use draft, current or superseded")
        if name != "README.md" and " — " not in (top_heading(text) or ""):
            err(rel(path), "top heading should read '<Project> — <Component> <doc type>' (STANDARD.md, Titles)")


def check_links(path):
    text = read(path)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    for target in LINK.findall(text):
        if re.match(r"^(https?:|mailto:|#)", target):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        dest = os.path.normpath(os.path.join(os.path.dirname(path), target))
        if not os.path.exists(dest):
            err(rel(path), f"link to {target} doesn't resolve")


def headings(path):
    return [line[3:].strip() for line in read(path).splitlines() if line.startswith("## ")]


def check_readme_sections(readme, template):
    """A README has every section its template has. Extra sections are fine."""
    if not os.path.exists(readme):
        return
    have = set(headings(readme))
    template_readme = os.path.join(ROOT, "_template", template, "README.md")
    for heading in headings(template_readme):
        if heading not in have:
            err(rel(readme), f"missing the '## {heading}' section from _template/{template}/README.md")


def is_component(path):
    return os.path.isdir(path) and os.path.basename(path) != "images"


def check_sensitive(path, text):
    if SYNC_HEADER.search(text):
        err(rel(path), 'has a "Synced from Claude Docs" header')
    if EMAIL.search(text):
        err(rel(path), "contains an email address")
    for pattern in SECRET_MARKERS:
        if pattern.search(text):
            err(rel(path), "contains an obvious secret marker")
            break


def iter_text_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [name for name in dirnames if name != ".git"]
        for name in filenames:
            yield os.path.join(dirpath, name)


def main():
    projects = sorted(
        name for name in os.listdir(ROOT)
        if os.path.isdir(os.path.join(ROOT, name))
        and name not in SKIP_DIRS
        and not name.startswith(".")
    )

    for proj in projects:
        pdir = os.path.join(ROOT, proj)
        for req in PROJECT_REQUIRED:
            if not os.path.exists(os.path.join(pdir, req)):
                err(proj, f"project is missing {req}")
        check_readme_sections(os.path.join(pdir, "README.md"), "project")
        check_markdown(pdir)
        for name in sorted(os.listdir(pdir)):
            path = os.path.join(pdir, name)
            if os.path.isfile(path) and name.endswith(".md") and name not in PROJECT_REQUIRED and name not in PROJECT_OPTIONAL:
                warn(rel(path), "not a named project-level type in STANDARD.md")
        for name in sorted(os.listdir(pdir)):
            cdir = os.path.join(pdir, name)
            if not is_component(cdir):
                continue
            for req in COMPONENT_REQUIRED:
                if not os.path.exists(os.path.join(cdir, req)):
                    err(rel(cdir), f"component is missing {req}")
            check_readme_sections(os.path.join(cdir, "README.md"), "component")
            check_markdown(cdir)
            for filename in sorted(os.listdir(cdir)):
                if (
                    filename.endswith(".md")
                    and filename not in COMPONENT_REQUIRED
                    and not COMPONENT_OPTIONAL_RE.match(filename)
                ):
                    warn(
                        rel(os.path.join(cdir, filename)),
                        "not a required or named optional component type in STANDARD.md",
                    )

    readme_path = os.path.join(ROOT, "README.md")
    if not os.path.exists(readme_path):
        err("README.md", "missing")
    else:
        readme = read(readme_path)
        for proj in projects:
            if f"]({proj}/)" not in readme:
                err("README.md", f"doesn't link the {proj}/ project")

    # Links everywhere except the templates, whose links are written for copies.
    # Placeholder text lives in _template/ and is not checked here either.
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [name for name in dirnames if name not in {".git", "_template"}]
        for filename in filenames:
            if filename.endswith(".md"):
                check_links(os.path.join(dirpath, filename))

    for path in iter_text_files():
        text = read_text(path)
        if text is not None:
            check_sensitive(path, text)

    for line in errors + warnings:
        print(line)
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s) across {len(projects)} project(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
