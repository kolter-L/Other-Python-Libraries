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

You need to add an app password by going to [This Link](https://bitbucket.org/account/settings/)

You can use this when pushing to the repo

You can also configure your repo to use SSH which is better -> [SSH on Mac](https://support.atlassian.com/bitbucket-cloud/docs/set-up-personal-ssh-keys-on-macos/)

## GIT: How to change the name of a directory (When it does not seem to be working)

DO NOT DO THIS: `** just changes the name of the directory in VS Code by clicking on it (stupid) **`

This will result in git tracking both the new and old directories. It will push the new one with the rename, and both will end up in your remote repo (duplicates).

Instead, do this: `git mv <old_file_name> <new_file_name>`

This will move the files to the new file and avoid all the misfortunes of the first method of renaming
