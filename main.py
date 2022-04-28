#!/usr/bin/python3

import typer

app = typer.Typer()

@app.command()
def hello(name: str, iq: int):
    print(f"Hello {name}")
    print(f"Your iq is {iq}")

@app.command()
def goodbye():
    print("Goodbye!")

if __name__ == "__main__":
    app()
