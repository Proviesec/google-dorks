#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Check query-list formatting without making live search requests."""

from pathlib import Path
import sys


root = Path(__file__).resolve().parents[1]
errors = []
files = sorted(root.rglob("*.txt"))

for path in files:
    relative = path.relative_to(root)
    lines = path.read_text(encoding="utf-8").splitlines()
    if not any(line.strip() and not line.lstrip().startswith("#") for line in lines):
        errors.append(f"{relative}: no queries")
    seen = {}
    for number, line in enumerate(lines, 1):
        location = f"{relative}:{number}"
        if line != line.rstrip():
            errors.append(f"{location}: trailing whitespace")
        query = line.strip()
        if not query or query.startswith("#"):
            continue
        if query in seen:
            errors.append(f"{location}: duplicate of line {seen[query]}")
        seen[query] = number
        if "filetyp:" in query:
            errors.append(f"{location}: use filetype:")
        # The historical archive has many unreviewed, malformed quotes.
        if relative.name != "all-google-dorks.txt" and query.count('"') % 2:
            errors.append(f"{location}: unmatched double quote")

for error in errors:
    print(error, file=sys.stderr)
print(f"Checked {len(files)} query files; {len(errors)} issue(s).")
sys.exit(bool(errors))
