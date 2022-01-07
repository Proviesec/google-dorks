# google-dorks

<a href="https://proviesec.org/">
    <img src="https://avatars.githubusercontent.com/u/92156402?s=400&u=7fe0dbb9085a37818ee8c2b061432a9a69cbff42&v=4" alt="Proviesec logo" title="Proviesec" align="right" height="60" />
</a>
<a href="https://www.buymeacoffee.com/proviesec" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>


# Introduction 

:star: Star us on GitHub — it motivates a lot! :star:

If you have any google dork, just create a PullRequest. 

# Ideas

- [ ] log file dorks
- [ ] best reports
- [ ] finding aws secrets 
- [ ] js secrets 



# GitHub Dorks for Finding Files

- filename:manifest.xml
- filename:travis.yml
- filename:vim_settings.xml
- filename:database
- filename:prod.exs NOT prod.secret.exs
- filename:prod.secret.exs
- filename:.npmrc _auth
- filename:.dockercfg auth
- filename:WebServers.xml
- filename:.bash_history <Domain name>
- filename:sftp-config.json
- filename:sftp.json path:.vscode
- filename:secrets.yml password
- filename:.esmtprc password
- filename:passwd path:etc
- filename:dbeaver-data-sources.xml
- path:sites databases password
- filename:config.php dbpasswd
- filename:prod.secret.exs
- filename:configuration.php JConfig password
- filename:.sh_history
- shodan_api_key language:python
- filename:shadow path:etc
- JEKYLL_GITHUB_TOKEN
- filename:proftpdpasswd
- filename:.pgpass
- filename:idea14.key
- filename:hub oauth_token
- HEROKU_API_KEY language:json
- HEROKU_API_KEY language:shell
- SF_USERNAME salesforce
- filename:.bash_profile aws
- extension:json api.forecast.io
- filename:.env MAIL_HOST=smtp.gmail.com
- filename:wp-config.php
- extension:sql mysql dump
- filename:credentials aws_access_key_id
- filename:id_rsa or filename:id_dsa
    
# GitHub Dorks for Finding Languages
language:python username
language:php username
language:sql username
language:html password
language:perl password
language:shell username
language:java api
HOMEBREW_GITHUB_API_TOKEN language:shell

# GiHub Dorks for Finding API Keys, Tokens and Passwords
api_key
“api keys”
authorization_bearer:
oauth
auth
authentication
client_secret
api_token:
“api token”
client_id
password
user_password
user_pass
passcode
client_secret
secret
password hash
OTP
user auth

# GitHub Dorks for Finding Usernames
user:name (user:admin)
org:name (org:google type:users)
in:login (<username> in:login)
in:name (<username> in:name)
fullname:firstname lastname (fullname:<name> <surname>)
in:email (data in:email)

#GitHub Dorks for Finding Information using Dates
created:<2012–04–05
created:>=2011–06–12
created:2016–02–07 location:iceland
created:2011–04–06..2013–01–14 <user> in:username

# GitHub Dorks for Finding Information using Extension
extension:pem private
extension:ppk private
extension:sql mysql dump
extension:sql mysql dump password
extension:json api.forecast.io
extension:json mongolab.com
extension:yaml mongolab.com
[WFClient] Password= extension:ica
extension:avastlic “support.avast.com”
extension:json googleusercontent client_secret
