# Google Dorks for web security

A collection of search queries for finding publicly indexed pages, files, and technology footprints during authorized security work. A search result is a lead to investigate, **not proof of a vulnerability**. Google results can be incomplete, personalized, or change over time.

## Start here

1. Choose a topic in the [catalog](CATALOG.md). For a shorter starting set, open [best-google-dorks.txt](best-google-dorks.txt).
2. Limit the query to a domain you own or are authorized to assess. For example, adapt a query to `site:example.com filetype:env "DB_PASSWORD"` by replacing `example.com` with your in-scope domain. Check the program's rules before searching related domains or third-party services.
3. Verify any result manually. A matching title, filename, parameter, or login page does not establish exposure or exploitability. If you find sensitive data, do not copy it into an issue or pull request; notify the owner privately.

The [all-google-dorks.txt](all-google-dorks.txt) file is a **historical, unverified archive**. It contains old product fingerprints and queries that may no longer work. Do not treat its size or an entry's presence as evidence of current usefulness.

## Find the right list

| Goal | Start with |
| --- | --- |
| Common file and configuration exposure checks | [Short starting list](best-google-dorks.txt), [environment files](google-dorks-for-env-files.txt), [backups](google-dorks-for-backups.txt) |
| Cloud and service configuration | [Cloud lists in the catalog](CATALOG.md#cloud-services-and-credentials) |
| CMS and web server footprints | [CMS](CATALOG.md#content-management-systems), [web servers](CATALOG.md#web-servers-and-technologies) |
| AI applications and agents | [Gemini](google-dorks-for-gemini.txt), [OpenAI](google-dorks-for-openai.txt), [AI agents](google-dorks-for-ai-agents.txt), [AI guidance](docs/ai-and-agent-search.md) |
| Bug bounty program discovery | [Program queries](google-dorks-for-bug-bounty-programs.txt) |

See the [full catalog](CATALOG.md) for every query file and its purpose. Existing filenames are kept stable so external links continue to work; some contain historic spelling or category names.

## Search syntax

Google documents `site:`, `filetype:`, quoted phrases, exclusion with `-`, and `before:`/`after:` in its [search help](https://support.google.com/websearch/answer/2466433). Put no space between an operator and its value. For example:

```text
site:example.com filetype:pdf "internal"
site:example.com "login" -inurl:blog
```

Some older queries use operators or wildcard patterns that are not documented for current Google Search. The former `cache:` operator no longer works ([Google's update](https://developers.google.com/search/updates)). If a query gives surprising results, simplify it and check the current documentation. `site:` results are not an exhaustive inventory of indexed URLs ([Google Search Central](https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site)).

## Interpret results carefully

- A search result for a login page indicates a page, not weak authentication.
- A URL parameter indicates an input to review, not SQL injection, XSS, or open redirect. The filenames for those lists are retained for compatibility.
- A public prompt or agent configuration is not automatically confidential. A key name is not an actual credential.
- Never publish real credentials, private data, or a live target's sensitive URL in contributions.

## For site owners

Keep private content behind authentication and authorization, remove accidentally published files, and rotate any exposed credentials. Use `noindex` only to keep otherwise public content out of search results; it does not restrict access. `robots.txt` controls crawler access and does not protect secrets: blocked URLs may still appear in results. See [Google's guidance](https://developers.google.com/search/docs/crawling-indexing/robots/intro) and the [safe-use guide](docs/safe-use.md).

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md) before suggesting a query. Include its purpose, expected signal, likely false positives, and a documentation or public reference when possible. AI-generated suggestions require human review. The repository's small offline check catches duplicate lines and common formatting mistakes; it does not claim to validate live Google results.

## License and attribution

The query lists (`*.txt`) and project documentation (`*.md`) are licensed under [Creative Commons Attribution 4.0 International](LICENSE). You may copy, change, and redistribute them, including commercially. When sharing licensed material, credit **Proviesec** as the source, link to [this repository](https://github.com/Proviesec/google-dorks) and the [license](https://creativecommons.org/licenses/by/4.0/), and indicate if you made changes. The license applies where copyright or database rights exist; it does not create rights over unprotected facts or short search terms.

The Python checker and GitHub Actions workflow are licensed separately under the [MIT License](LICENSE-CODE). Reuse of that code requires keeping its copyright and license notice.

Maintained by [Proviesec](https://proviesec.de/). You can support the project through the links in [.github/FUNDING.yml](.github/FUNDING.yml).
