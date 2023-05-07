student@ubuntu224-18:~$ mkdir -p workspace/Koraik/nauka_gita
student@ubuntu224-18:~$ cd workspace/Koraik/nauka_gita/
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ 
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git config -l
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git config --global user.email "koraik@users.noreply.github.com"
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ car ~/.gitconfig

student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ atom .
2023/05/07 09:59:23.370097 cmd_run.go:616: WARNING: XAUTHORITY environment value is not a clean path: "/run/gdm3/auth-for-student-SPUN41/database"
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git add README.md
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git commit -m "dodanie readme"
[master (root-commit) 371bc77] dodanie readme
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git push
fatal: No configured push destination.
Either specify the URL from the command-line or configure a remote repository using

    git remote add <name> <url>

and then push using the remote name

    git push <name>

student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git status
On branch master
nothing to commit, working tree clean
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git log
commit 371bc771066952a35cb595bfd83d541f40e0c069 (HEAD -> master)
Author: student <koraik@users.noreply.github.com>
Date:   Sun May 7 10:01:29 2023 +0200

    dodanie readme

student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git remote add origin https://github.com/Koraik/nauka_gita.git
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git push -u origin main
Username for 'https://github.com': Koraik
Password for 'https://Koraik@github.com': 
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/Koraik/nauka_gita.git/'
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git push -u origin main
Username for 'https://github.com': Koraik
Password for 'https://Koraik@github.com': 
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/Koraik/nauka_gita.git/'
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ cat ~/.gitconfig
[user]
	email = koraik@users.noreply.github.com
	name = Koraik
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git config -l
user.email=koraik@users.noreply.github.com
user.name=Koraik
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
remote.origi.url=https://.../nauka_gita.git
remote.origi.fetch=+refs/heads/*:refs/remotes/origi/*
remote.orgin.url=https://github.com/Koraik/nauka_gita.git
remote.orgin.fetch=+refs/heads/*:refs/remotes/orgin/*
remote.origin.url=https://github.com/Koraik/nauka_gita.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git config --global user.email "Koraik@users.noreply.github.com"
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ cat ~/.gitconfig

student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git push -u origin main
Username for 'https://github.com': Koraik
Password for 'https://Koraik@github.com': 
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 220 bytes | 110.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/Koraik/nauka_gita.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git remote -v
orgin	https://github.com/Koraik/nauka_gita.git (fetch)
orgin	https://github.com/Koraik/nauka_gita.git (push)
origi	https://.../nauka_gita.git (fetch)
origi	https://.../nauka_gita.git (push)
origin	https://github.com/Koraik/nauka_gita.git (fetch)
origin	https://github.com/Koraik/nauka_gita.git (push)
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git status
On branch main
Your branch is up to date with 'origin/main'.

curllll
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ curl --fail -X POST \
> -H "Content-Type: application/json" \
> -d '{"name":"natalia"}' https://httpbin.org/post
{
  "args": {}, 
  "data": "{\"name\":\"natalia\"}", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Content-Length": "18", 
    "Content-Type": "application/json", 
    "Host": "httpbin.org", 
    "User-Agent": "curl/7.68.0", 
    "X-Amzn-Trace-Id": "Root=1-64576d96-4da7b020210ffa840428f27f"
  }, 
  "json": {
    "name": "natalia"
  }, 
  "origin": "156.17.55.193", 
  "url": "https://httpbin.org/post"
}
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ curl --fail -X POST \
> -H "Content-Type: application/json" \
> -d '{"name":"natalia"}' https://httpbin.org/get
curl: (22) The requested URL returned error: 405 

student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ curl --fail -X GET \
> -H "Content-Type: application/json" \
> https://httpbin.org/get
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Content-Type": "application/json", 
    "Host": "httpbin.org", 
    "User-Agent": "curl/7.68.0", 
    "X-Amzn-Trace-Id": "Root=1-64576e3e-3d2a167970b909c812d74a04"
  }, 
  "origin": "156.17.55.193", 
  "url": "https://httpbin.org/get"
}
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ curl --fail \
> -X DELETE \
> -H "Content-Type: application/json" https://httpbin.org/delete
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Content-Type": "application/json", 
    "Host": "httpbin.org", 
    "User-Agent": "curl/7.68.0", 
    "X-Amzn-Trace-Id": "Root=1-64576e95-5db01fef24773f163c3cc9ca"
  }, 
  "json": null, 
  "origin": "156.17.55.193", 
  "url": "https://httpbin.org/delete"
}


