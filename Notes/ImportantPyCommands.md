## VENV

Create new Venv: `python -m venv venv`

Start Venv: `source venv/bin/activate`

## GIT: It's pushing stuff that you don't want to be pushed

1. Add the file to .gitignore

2. If it's already tracked, you have to remove it with this:

    `git rm -r --cached <file_you_dont_want>`

3. Then you have to delete it from the Repo if you've already pushed it
4. Run this command to force a push:

    `git push origin main --force`