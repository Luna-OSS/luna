"""Get the IP address of the client."""

import typer
import requests

app = typer.Typer()

@app.command()
def main():
    """Shows the IP address of the client."""
    print(requests.get('https://checkip.amazonaws.com', timeout=5).text.strip())

if __name__ == '__main__':
    typer.run(main)
