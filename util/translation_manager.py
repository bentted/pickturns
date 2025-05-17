"""
Translation Manager

A utility for those maintaining and contributing to the translation of this project.

-Figgy (jack-adorbs)
"""

import click
import json

@click.Group
def cli():
    pass

@cli.command
def find():
    pass

if __name__ == "__main__":
    cli()