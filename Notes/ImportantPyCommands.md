## VENV

Create new Venv: `python -m venv venv`

Start Venv: `source venv/bin/activate`

## Save dependencies to requirements.txt

Create requirements.txt: `pip freeze > requirements.txt`

Reinstall in new ENV: `pip install -r requirements.txt`

## Not getting the homebrew VENV Instance

Create the venv with: `/opt/homebrew/bin/python3.13 -m venv venv`

Check python being used: `which python`

Check version with: python `--version`
