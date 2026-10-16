# Contributing queries

Thanks for improving the collection. Keep a pull request focused on one topic or a small set of related queries.

For each new query or correction, explain:

1. What it is intended to find and which file should contain it.
2. What a matching result actually indicates, including common false positives.
3. A public product or search-operator reference, when available.
4. Whether you tested the syntax with an asset you own or are authorized to assess, and when. Do not include the target or result if it contains private information.

Prefer short, distinct queries. Keep one query per line in `.txt` files; use `#` only for section headings in curated lists. Avoid copies of existing lines, trailing whitespace, real credentials, and private targets. `example.com` is the placeholder for scoped examples. Do not claim that a URL parameter or product fingerprint proves a vulnerability.

Run `python3 scripts/check_dorks.py` before submitting. It checks local formatting and duplicate lines, not search effectiveness. Google results vary, so a reviewer must still judge usefulness and scope. AI-generated queries need the same human verification as any other contribution.

Report a live exposure privately to the affected owner. Do not open a public issue with secrets, personal data, or sensitive URLs. See [safe use](docs/safe-use.md).
