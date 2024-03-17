# google-dorks
[![License](https://img.shields.io/badge/license-MIT-_red.svg)](https://opensource.org/licenses/MIT)
![contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)
<img src="https://img.shields.io/github/stars/Proviesec/google-dorks?style=social"> <img src="https://img.shields.io/github/forks/Proviesec/google-dorks?style=social">
<a href="https://proviesec.org/">
    <img src="https://avatars.githubusercontent.com/u/92156402?s=400&u=7fe0dbb9085a37818ee8c2b061432a9a69cbff42&v=4" alt="Proviesec logo" title="Proviesec" align="right" height="60" />
</a>
[![Twitter](https://img.shields.io/twitter/follow/proviesec?label=Follow)](https://twitter.com/proviesec)
<a href="https://www.buymeacoffee.com/proviesec" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
<a href="https://patreon.com/proviesec"><img src="https://user-images.githubusercontent.com/6010786/178968010-4d47859d-ef52-4d0e-85eb-549654f9ad65.jpg" alt="Buy Me A Coffee" height="80"></a>
Read this, my Medium Blog Space:👩‍💻<a href="https://proviesec.medium.com/"><b>Proviesec Security Medium Articles - read it</b></a>

Table of Contents
------------
* [Introduction](#introduction)
* [My love google dork](#my-love-google-dork)
* [Search filters](#search-filters)
* [Operators](#operators)
   * [Search Term](#search-term)
   * [OR](#or)
* [Ideas](#ideas)
* [Links](#links)
* [Example](#example)
* [Preventing GOOGLE DORKS](#preventin-google-dorks)

# Introduction 

:star: Star us on GitHub — it motivates a lot! :star:

**If you have any google dork, just create a PullRequest or wrtie me on twitter.**  [![Twitter](https://img.shields.io/twitter/follow/proviesec?label=Follow)](https://twitter.com/proviesec) 

**My medium article about Google Dorks** [How to use google dorks](https://medium.com/@proviesec/google-dork-the-best-one-and-how-do-you-find-bugs-with-it-689c69804b81)  


# My love google dork
```
intext:"index of" "parent directory"
```

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
site:twitter.com +site:twitter.*
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
- [x] Git google dorks
- [x] phpmyadmin google dorks
- [x] phpinfo google dorks
- [x] log file google dorks
- [x] google dorks for excel files
- [ ] Google Dorks for presentations 
- [ ] best google dorks reports 
- [x] finding aws secrets with google dorks
- [ ] js secrets with google dorks
- [ ] CMS google dorks
  - [x] Wordpress
  - [x] Typo3
  - [x] Magento
  - [x] Joomla
  - [ ] Drupal
  - [ ] Shopify
- [x] Admin google dorks
- [x] Monitoring pages - google dorks
- [ ] Google Dorks - Github page


# Links

- exploit-db.com
- nvd.nist.gov
- cxsecurity.com
- vulnerability-lab.com 

# Writeups

https://infosecwriteups.com/my-first-reflected-xss-bug-bounty-google-dork-xxx-92ac1180e0d0
https://dewangpanchal98.medium.com/microsoft-bug-bounty-writeup-5ee4a7264dbf

# Example 

![image](https://user-images.githubusercontent.com/6010786/152770177-537fbfa2-235e-4951-a885-12c6a90c40a5.png)

## Preventing GOOGLE DORKS

Encoding/encrypting sensitive data such as usernames, passwords and so forth.
Run inquiries against your own site to check whether you can locate any sensitive data. On the off chance that you discover sensitive information, you can remove it from search results by utilizing Google Search Console.
Protect sensitive content by utilizing a robots.txt document situated in your root-level site catalog. 
Utilizing robots.txt helps prevent Google from indexing our site, but it can also show an attacker where sensitive data might be located.
User-agent: * 
Disallow: / 

You can also block specific directories to be excepted from web crawling. 
If you have the /phpinfo site and you need to protect it, just place this code inside:

User-agent: *   
Disallow: /phpinfo/ 


Restrict access to specific files:

User-agent: *   
Disallow: /member/info.html 

Restrict access to dynamic URLs that contain ? symbol:

User-agent: *   
Disallow: /*?  


# Disclaimer: DONT BE A JERK!
Needless to mention, please use this tool very very carefully. The authors won't be responsible for any consequences.
