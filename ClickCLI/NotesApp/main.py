import click
import json
import os

NOTES_FILE = 'notes.json'

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
@click.option('--comment', '-c', default='', help='Optional comment')
def add(name, comment):
    notes = load_notes()
    note = f"{name}: {comment}" if comment else name
    notes.append(note)
    save_notes(notes)
    click.echo(f"Note added: {note}")

@cli.command(name='list')
def list_notes():
    notes = load_notes()
    if not notes:
        click.echo("No notes yet.")
    else:
        click.echo("Notes:")
        for i, note in enumerate(notes, 1):
            click.echo(f"{i}. {note}")


@cli.command()
@click.argument('index')
def delete(index):
    notes = load_notes()
    try:
        del notes[int(index)]
    except ValueError:
        click.echo("You've gotta enter an integer")
        return
    except IndexError:
        click.echo("That is not a valid index")
        return
    save_notes(notes)
    click.echo(f"Note at index {index} was deleted.")

if __name__ == '__main__':
    cli()
