# Query catalog

All `.txt` files contain candidate search queries, not verified findings. Most lists have not been tested against current Google results. Start with the smaller lists; use the historical archive for reference only. Add `site:example.com` with a domain you are authorized to assess where appropriate.

## Starting points and archives

- [best-google-dorks.txt](best-google-dorks.txt) — short starting collection; section labels describe topics, not measured effectiveness.
- [google-dorks-best-log.txt](google-dorks-best-log.txt) — log and error-page candidates.
- [all-google-dorks.txt](all-google-dorks.txt) — historical archive; includes obsolete and malformed entries.

## AI and agents

- [google-dorks-for-gemini.txt](google-dorks-for-gemini.txt) — Gemini API configuration and application markers.
- [google-dorks-for-openai.txt](google-dorks-for-openai.txt) — OpenAI configuration and code markers; includes legacy SDK terms.
- [google-dorks-for-anthropic.txt](google-dorks-for-anthropic.txt) — Anthropic configuration markers.
- [google-dorks-for-cohere.txt](google-dorks-for-cohere.txt) — Cohere configuration markers.
- [google-dorks-for-ai-agents.txt](google-dorks-for-ai-agents.txt) — public agent instructions and tool configuration markers.

See [AI and agent search](docs/ai-and-agent-search.md) for how to interpret these results.

## Cloud services and credentials

- [google-dorks-for-azure.txt](google-dorks-for-azure.txt) — Azure configuration and storage references.
- [google-dorks-for-backups.txt](google-dorks-for-backups.txt) — backup filenames and directory listings.
- [google-dorks-for-ci-cd.txt](google-dorks-for-ci-cd.txt) — CI configuration markers.
- [google-dorks-for-cloud-platforms.txt](google-dorks-for-cloud-platforms.txt) — cloud platform configuration names.
- [google-dorks-for-conf.txt](google-dorks-for-conf.txt) — configuration filenames and terms.
- [google-dorks-for-database-files.txt](google-dorks-for-database-files.txt) — database file names and dumps.
- [google-dorks-for-discord.txt](google-dorks-for-discord.txt) — Discord configuration markers.
- [google-dorks-for-env-files.txt](google-dorks-for-env-files.txt) — environment variable names.
- [google-dorks-for-finding-aws-s3.txt](google-dorks-for-finding-aws-s3.txt) — S3-related search candidates, some historical.
- [google-dorks-for-firebase.txt](google-dorks-for-firebase.txt) — Firebase configuration markers; a public `apiKey` alone is not proof of exposure.
- [google-dorks-for-gcp.txt](google-dorks-for-gcp.txt) — Google Cloud configuration markers.
- [google-dorks-for-git-files.txt](google-dorks-for-git-files.txt) — Git metadata and directory listings.
- [google-dorks-for-github-actions.txt](google-dorks-for-github-actions.txt) — workflow file markers.
- [google-dorks-for-js-secrets.txt](google-dorks-for-js-secrets.txt) — JavaScript-related secret terms.
- [google-dorks-for-mailgun.txt](google-dorks-for-mailgun.txt) — Mailgun configuration markers.
- [google-dorks-for-mongodb.txt](google-dorks-for-mongodb.txt) — MongoDB configuration markers.
- [google-dorks-for-sendgrid.txt](google-dorks-for-sendgrid.txt) — SendGrid configuration markers.
- [google-dorks-for-slack.txt](google-dorks-for-slack.txt) — Slack configuration markers.
- [google-dorks-for-stripe.txt](google-dorks-for-stripe.txt) — Stripe configuration markers; publishable keys are not secrets.
- [google-dorks-for-twilio.txt](google-dorks-for-twilio.txt) — Twilio configuration markers.
- [finding-username-passwords/google-dorks-for-aws-passwords.txt](finding-username-passwords/google-dorks-for-aws-passwords.txt) — AWS credential names.
- [finding-username-passwords/google-dorks-for-mysql-passwords.txt](finding-username-passwords/google-dorks-for-mysql-passwords.txt) — MySQL credential terms.
- [finding-username-passwords/google-dorks-for-postgres-passwords.txt](finding-username-passwords/google-dorks-for-postgres-passwords.txt) — PostgreSQL credential and error terms.

## Content management systems

- [cms/google-dorks-contao.txt](cms/google-dorks-contao.txt) — Contao paths.
- [cms/google-dorks-for-blogengine.txt](cms/google-dorks-for-blogengine.txt) — BlogEngine.NET fingerprints, many for an old release.
- [cms/google-dorks-for-drupal.txt](cms/google-dorks-for-drupal.txt) — Drupal fingerprints.
- [cms/google-dorks-for-joomla.txt](cms/google-dorks-for-joomla.txt) — Joomla fingerprints, including old versions.
- [cms/google-dorks-for-typo3.txt](cms/google-dorks-for-typo3.txt) — TYPO3 fingerprints.
- [cms/google-dorks-for-wordpress.txt](cms/google-dorks-for-wordpress.txt) — WordPress paths and directory listings.
- [cms/google-dorks-magento.txt](cms/google-dorks-magento.txt) — Magento paths, mainly historical Magento 1 conventions.

## Web servers and technologies

- [google-dorks-for-frameworks.txt](google-dorks-for-frameworks.txt) — frontend framework configuration terms.
- [google-dorks-for-grafana.txt](google-dorks-for-grafana.txt) — Grafana pages.
- [google-dorks-for-kibana.txt](google-dorks-for-kibana.txt) — Kibana path.
- [google-dorks-for-kubernetes.txt](google-dorks-for-kubernetes.txt) — Kubernetes and application health endpoints.
- [google-dorks-for-monitoring.txt](google-dorks-for-monitoring.txt) — monitoring pages.
- [google-dorks-for-stats.txt](google-dorks-for-stats.txt) — statistics pages, including legacy URLs.
- [google-dorks-for-swagger.txt](google-dorks-for-swagger.txt) — OpenAPI and Swagger pages.
- [google-dorks-for-webserver.txt](google-dorks-for-webserver.txt) — broad, mostly historical server fingerprints.
- [technology/google-dorks-for-ftp.txt](technology/google-dorks-for-ftp.txt) — FTP listings.
- [technology/google-dorks-for-java-sites.txt](technology/google-dorks-for-java-sites.txt) — Java page fingerprints.
- [technology/google-dorks-for-jira.txt](technology/google-dorks-for-jira.txt) — Jira pages.
- [technology/google-dorks-for-php-sites.txt](technology/google-dorks-for-php-sites.txt) — PHP URLs and pages.
- [web-server/best-webserver-google-dorks.txt](web-server/best-webserver-google-dorks.txt) — historical subset of server fingerprints, retained for existing links.
- [web-server/google-dorks-for-apache.txt](web-server/google-dorks-for-apache.txt) — Apache and Tomcat page fingerprints.
- [web-server/google-dorks-for-nginx.txt](web-server/google-dorks-for-nginx.txt) — Nginx page fingerprints and scoped examples.
- [web-server/google-dorks-for-phpmyadmin.txt](web-server/google-dorks-for-phpmyadmin.txt) — phpMyAdmin page fingerprints.

## Discovery and documents

- [google-dorks-for-bug-bounty-programs.txt](google-dorks-for-bug-bounty-programs.txt) — public disclosure and bounty program pages; verify the program's actual scope.
- [google-dorks-for-companys.txt](google-dorks-for-companys.txt) — organization mentions on third-party sites; historic filename retained for links.
- [google-dorks-for-excel-files.txt](google-dorks-for-excel-files.txt) — spreadsheets.
- [google-dorks-for-login.txt](google-dorks-for-login.txt) — login pages; presence is not a weakness.
- [google-dorks-for-open-redirect.txt](google-dorks-for-open-redirect.txt) — redirect-like URL parameters, not proven open redirects.
- [google-dorks-for-presentations.txt](google-dorks-for-presentations.txt) — slide files and presentations.
- [google-dorks-for-sql-injection.txt](google-dorks-for-sql-injection.txt) — parameterized URLs, not proven SQL injection.
- [google-dorks-for-wikipedia.txt](google-dorks-for-wikipedia.txt) — wiki and MediaWiki footprints.
- [google-dorks-for-xss.txt](google-dorks-for-xss.txt) — parameterized URLs, not proven XSS.
