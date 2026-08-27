#!/usr/bin/env python3
"""Validate the distributable production-web-standard skill."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "production-web-standard"


def fail(message: str) -> None:
    raise SystemExit(f"Validation failed: {message}")


def main() -> None:
    entrypoint = SKILL_DIR / "SKILL.md"
    ui_metadata = SKILL_DIR / "agents" / "openai.yaml"

    if not entrypoint.is_file():
        fail(f"missing {entrypoint.relative_to(ROOT)}")

    content = entrypoint.read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not frontmatter:
        fail("SKILL.md has no YAML frontmatter")

    metadata = frontmatter.group(1)
    if not re.search(r"^name:\s*production-web-standard\s*$", metadata, re.MULTILINE):
        fail("frontmatter name must be production-web-standard")
    if not re.search(r"^description:\s*\S", metadata, re.MULTILINE):
        fail("frontmatter description is missing")
    if re.search(r"\[(?:TODO|PLACEHOLDER)[^\]]*\]", content, re.IGNORECASE):
        fail("SKILL.md contains an unfinished scaffold placeholder")

    references = re.findall(r"\((references/[^)]+\.md)\)", content)
    if not references:
        fail("SKILL.md links no references")
    for reference in references:
        if not (SKILL_DIR / reference).is_file():
            fail(f"missing linked reference: {reference}")

    if not ui_metadata.is_file():
        fail("missing agents/openai.yaml")
    ui_content = ui_metadata.read_text(encoding="utf-8")
    if "$production-web-standard" not in ui_content:
        fail("default prompt must mention $production-web-standard")

    print("production-web-standard is valid")


if __name__ == "__main__":
    main()
