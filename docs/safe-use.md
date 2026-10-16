# Safe use and response

Use these queries only on assets you own or are authorized to assess. Check the target's published scope and rules. Search results are leads; verify them without accessing more data than needed to establish and report an issue.

If a result appears to contain a credential or private information, do not paste it into a public issue, pull request, screenshot, or chat. Notify the affected owner through their security contact or disclosure program. Site owners should remove or restrict the exposed source, revoke or rotate affected credentials, and then address search indexing. Removing a search result alone does not fix exposure.

`robots.txt` can limit crawling but is not an access-control mechanism. A blocked URL can still appear in Google results when other pages link to it. Private content needs authentication or removal. A `noindex` directive can keep otherwise public content out of search results, but visitors with its URL can still access it. See [Google's robots.txt guidance](https://developers.google.com/search/docs/crawling-indexing/robots/intro) and [content-control guidance](https://developers.google.com/search/docs/crawling-indexing/control-what-you-share).
