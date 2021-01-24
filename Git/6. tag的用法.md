## Git中tag的用法

###### 1. tag的含义

tag是对一个commit ID的引用。通常用于给开发分支做一个标记，如标记一个版本号。

###### 2. 切换到指定tag

`git checkout 1.0`

###### 3. 打标签

`git tag -a v1.01 -m "Release version 1.01"`

> 注:`git tag`是打标签的命令, `-a`是添加标签, 后面跟标签名字, `-m` 及后面的字符串是对该标签的注释

###### 4. 提交标签到远程仓库

`git push origin --tags`

> 注: 就像`git push origin master`把本地修改提交到远程仓库一样, `-tags`可以把本地打的标签全部提交到远程仓库

###### 5. 删除标签

`git tag -d v1.01`

> 注: `-d`表示删除, 后面跟要删除的`tag`的名字

###### 6. 删除远程标签

`git push origin :refs/tags/v1.01`

> 注: 就像`git push origin :branch_1 可以删除远程仓库的分支branch_1一样,冒号前为空表示删除远程仓库的tag

###### 7. 查看标签

`git tag`

或

`git tag -l`

###### 8. 把标签同步到服务器

默认情况下, `git push`并不会把tag标签推送到服务器, 只有通过显式命令才能分享标签到远端仓库.

1. push单个tag, 命令格式为: `git push origin [tagname]`

> 例如: `git push origin v1.0` 把本地v1.0的tag推送到远端服务器

2. push所有tag, 命令格式为: `git push [origin] --tags`

> 例如: `git push --tags`
>
> 或: `git push origin --tags`

###### 9. 注意

如果要在tag代码的基础上做修改,需要在tag处新建一个分支:

> `git checkout -b branch_name tag_name`
>
> 这样会从tag创建一个分支进行修改.



