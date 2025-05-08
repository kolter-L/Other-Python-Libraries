import click
import subprocess

@click.group()
def cli():
    """API Test CLI"""
    pass

@cli.command()
@click.option('--base-url', default='http://localhost:3000', help='Base URL of the API')
# THE BASE_URL VARIABLE IS DEFINED IN CONFTEST.PY
def test(base_url):
    """Run all API tests against a given base URL"""
    click.echo(f"Running tests against: {base_url}")

    # Pass base_url as a flag to the pytest sub process
    subprocess.run(['pytest', '-s', '--base-url', base_url])

if __name__ == '__main__':
    cli()
