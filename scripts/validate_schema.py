#!/usr/bin/env python3
"""Validate the structural contract of an academic visual schema."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = (
    "STYLE AND META-INSTRUCTIONS",
    "LAYOUT CONFIGURATION",
    "CONNECTIONS",
    "GLOBAL CONSTRAINTS",
)

META_LABELS = {
    "zone",
    "layout configuration",
    "container",
    "visual structure",
    "exact labels",
    "connections",
    "global constraints",
}


def validate(text: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    upper = text.upper()

    if "---BEGIN VISUAL SCHEMA---" not in upper:
        errors.append("missing ---BEGIN VISUAL SCHEMA--- marker")
    if "---END VISUAL SCHEMA---" not in upper:
        errors.append("missing ---END VISUAL SCHEMA--- marker")

    for section in REQUIRED_SECTIONS:
        if f"[{section}]" not in upper:
            errors.append(f"missing [{section}] section")

    zones = re.findall(r"^\[ZONE\s+(\d+)\s*:[^\]]+\]", text, re.MULTILINE | re.IGNORECASE)
    if not 2 <= len(zones) <= 5:
        errors.append(f"expected 2-5 zones, found {len(zones)}")
    if len(zones) != len(set(zones)):
        errors.append("zone numbers must be unique")
    if zones and sorted(int(z) for z in zones) != list(range(1, len(zones) + 1)):
        errors.append("zone numbers must be contiguous starting at 1")

    for zone_number in zones:
        start_match = re.search(
            rf"^\[ZONE\s+{zone_number}\s*:[^\]]+\]",
            text,
            re.MULTILINE | re.IGNORECASE,
        )
        if not start_match:
            continue
        next_header = re.search(r"^\[(?:ZONE\s+\d+|CONNECTIONS|GLOBAL CONSTRAINTS)[^\]]*\]", text[start_match.end() :], re.MULTILINE | re.IGNORECASE)
        end = start_match.end() + next_header.start() if next_header else len(text)
        block = text[start_match.end() : end]
        for field in ("Container:", "Visual structure:", "Exact labels:"):
            if field.lower() not in block.lower():
                errors.append(f"zone {zone_number} missing {field[:-1]} field")

    connection_match = re.search(
        r"^\[CONNECTIONS\]\s*(.*?)(?=^\[GLOBAL CONSTRAINTS\])",
        text,
        re.MULTILINE | re.IGNORECASE | re.DOTALL,
    )
    if connection_match:
        numbered = re.findall(r"^\s*\d+\.\s+.+$", connection_match.group(1), re.MULTILINE)
        if not numbered:
            errors.append("CONNECTIONS must contain at least one numbered relationship")
        for index, item in enumerate(numbered, start=1):
            lowered = item.lower()
            if "from " not in lowered or " to " not in lowered:
                errors.append(f"connection {index} must state both 'From' and 'to' endpoints")

    unresolved = re.findall(r"<[^>]+>", text)
    if unresolved:
        errors.append(f"unresolved template placeholders: {', '.join(sorted(set(unresolved)))}")

    exact_label_lines = re.findall(r"^Exact labels:\s*(.*)$", text, re.MULTILINE | re.IGNORECASE)
    if not exact_label_lines:
        errors.append("no Exact labels fields found")
    for line in exact_label_lines:
        if line.strip().lower() not in {"none", '"none"'} and '"' not in line:
            errors.append(f"exact labels must be double-quoted or 'none': {line.strip()}")
        labels = re.findall(r'"([^"]+)"', line)
        for label in labels:
            if label.strip().lower() in META_LABELS or label.strip().lower().startswith("zone "):
                errors.append(f"meta-label must not be rendered: {label!r}")

    if "source support" not in text.lower() and "scientific invariant" not in text.lower():
        warnings.append("consider recording source support or scientific invariants")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("schema", type=Path, help="path to visual-schema.md")
    args = parser.parse_args()

    try:
        text = args.schema.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"ERROR: cannot read {args.schema}: {exc}", file=sys.stderr)
        return 2

    errors, warnings = validate(text)
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"INVALID: {len(errors)} error(s)", file=sys.stderr)
        return 1

    print(f"VALID: {args.schema} ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
