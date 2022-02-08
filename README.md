# google-dorks

<a href="https://proviesec.org/">
    <img src="https://avatars.githubusercontent.com/u/92156402?s=400&u=7fe0dbb9085a37818ee8c2b061432a9a69cbff42&v=4" alt="Proviesec logo" title="Proviesec" align="right" height="60" />
</a>
<a href="https://www.buymeacoffee.com/proviesec" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>


# Introduction 

:star: Star us on GitHub — it motivates a lot! :star:

If you have any google dork, just create a PullRequest. 


## Search filters

| Filter          | Description                                        | Example                              |
| :-------------- |:---------------------------------------------------| :------------------------------------|
| allintext      | Searches for occurrences of all specified keywords. | `allintext:"keyword"` |
| intext      | Searches for the occurrence of keywords at once or consecutively. | `intext:"keyword"` |
| intitle      | Searches for occurrences of keywords in the title all or one. | `intitle:"keyword"` |
| allintitle      | Searches for all occurrences of keywords at once. | `allintitle:"keyword"` |
| inurl      | Searches for a URL that matches one of the keywords. | `inurl:"keyword"` |
| allinurl      | Searches for a URL that matches all the keywords in the query. | `allinurl:"keyword"` |
| site      | Searches specifically for that particular website and lists all results for that website. | `site:"www.github.com"` |
| filetype      | Searches for a specific file type named in the query. | `filetype:"pdf"` |
| link      | Searches for external links to pages. | `link:"keyword"` |
| numrange      | Used to find specific numbers in your search. | `numrange:33-43` |
| before/after      | Used to search within a specified date range. | `filetype:pdf & (before:2021-01-01 after:2021-05-01)` |
| allinanchor (and also inanchor)      | This shows the websites that the keywords refer to in links, in order of most links. | `inanchor:rat` |
| allinpostauthor (and also inpostauthor)      | Exclusively for the blog search, blog posts written by specific people are picked out. | `allinpostauthor:"keyword"` |
| related      | List web pages that are "similar" to a given web page. | `related:www.github.com` |
| cache      | Displays the version of the web page that Google has in its cache. | `cache:www.github.com` |


## Operators
#### Search Term

This operator searches only for the exact term inside the quotation marks. You can use this for example if the term you are looking for is ambiguous and could easily be confused with something else, or if you don't get enough relevant results. 

Here is an example:

```
"Admin Loginpage"
```

#### OR
This operator searches for a specific search term OR another term.

```
site:instagram.com | site:github.com
```

#### AND
This operator searches for a specific search term and another term.

```
site:github.com & site:twitter.com
```

#### Operators combinaison
This operator combines search terms 
```
(site:instagram.com | site:twitter.com) (intext:"admin")
(site:instagram.com | site:twitter.com) & intext:"admin"
```

#### Include results

This will order results by the number of occurrence of the keyword.

```
-site:twitter.com +site:twitter.*
```

#### Exclude results

```
site:twitter.* -site:twitter.com
```

### Better Results (Subdomains)
```
site:*.site.com

site:*.*.site.com

site:*.*.*.site.com
```
#### Synonyms

```
~set
```

#### Glob pattern (*)

```
site:*.com
```

# Ideas

- [x] Git droks
- [ ] log file dorks
- [ ] best reports
- [ ] finding aws secrets 
- [ ] js secrets 
- [ ] CMS dorks
- [ ] Admin dorks

# Example 

![image](https://user-images.githubusercontent.com/6010786/152770177-537fbfa2-235e-4951-a885-12c6a90c40a5.png)

