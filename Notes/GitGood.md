## GIT: It's pushing stuff that you don't want to be pushed

1. Add the file to .gitignore

2. If it's already tracked, you have to remove it with this:

    `git rm -r --cached <file_you_dont_want>`

3. Then you have to delete it from the Repo if you've already pushed it
4. Run this command to force a push:

    `git push origin main --force`


## GIT: how to add a second remote repo

Type this with the name of the origin and the URL of the repo:

`git remote add bitbucket https://bitbucket.org/kolters-space/jiraapp`

To push to this other repo:

`git push bitbucket main`

To pull from this other repo:

`git pull bitbucket main`

## GIT: Bitbucket as remote repo

You need to add an app password by going to [text](https://bitbucket.org/account/settings/)

You can use this when pushing to the repo
