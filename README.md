weeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
weeeeeeee
woooooooooooooooooooooooooooooooooo
student@ubuntu224-18:~/tmp/nauka_gita$ curl --fail -X POST \
> -H "Content-Type: application/json" \
> -d '{"name":"natalia"}' https://httpbin.org/get
curl: (22) The requested URL returned error: 405 


student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git add README.md
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git -m 
unknown option: -m
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git commit -m
error: switch `m' requires a value
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git commit -m "a"
[main 893f1c0] a
 1 file changed, 2 insertions(+)
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git log
commit 893f1c0bd8e42525a7966352b91dc73a5fc8811c (HEAD -> main)
Author: Koraik <Koraik@users.noreply.github.com>
Date:   Sun May 7 10:41:37 2023 +0200

    a

commit 371bc771066952a35cb595bfd83d541f40e0c069 (origin/main)
Author: student <koraik@users.noreply.github.com>
Date:   Sun May 7 10:01:29 2023 +0200

    dodanie readme
student@ubuntu224-18:~/workspace/Koraik/nauka_gita$ git push
Username for 'https://github.com': Koraik
Password for 'https://Koraik@github.com': 
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 250 bytes | 250.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/Koraik/nauka_gita.git
   371bc77..893f1c0  main -> main
   
   aaaaa

