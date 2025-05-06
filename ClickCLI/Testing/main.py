import click

@click.command()
@click.argument('name')
@click.option('--comment', '-c', default='', help='Optional comment to include')
def greet(name, comment):
    """Greets a user and optionally includes a comment."""
    print(f"Hello, {name}!")
    if comment:
        print(f"Comment: {comment}")

if __name__ == '__main__':
    greet()
