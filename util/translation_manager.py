"""
Translation Manager

A utility for those maintaining and contributing to the translation of this project.

-Figgy (jack-adorbs)
"""
from pathlib import Path
import os
import json



LOC = Path(__file__)
RES = "res"

def read_json(file):
    res = None 
    with open(file, "r", encoding="utf8") as f:
        res = json.load(f)
    return res

def write_json(file, language):
    with open(file, "w", encoding="utf8") as f:
        json.dump(language, f, ensure_ascii=False)

def get_languages(dir):
    translations = (LOC.parents[1] / RES / dir)
    res = {}
    for translation in translations.iterdir():
        with open(translation, "r", encoding="utf-8") as f:
            res[translation.stem] = json.load(f)
    return res



def update(language, key, value):
    language[key] = value

if __name__ == "__main__":
    import click

    ctx = dict()
    os.chdir(LOC.parents[1] / RES)


    @click.group()
    @click.argument("filename", type=click.STRING)
    @click.argument("language", type=click.STRING)
    def cli(filename, language):
        # If language file names follow ISO standard could simiply parsing with 
        # iso639-lang lib.
        file = (Path(filename) / language).with_suffix(".json")
        language = read_json(file)
        ctx["language"] = language
        ctx["file"] = file 

    @cli.command("insert")
    @click.argument("key", type=click.STRING)
    @click.argument("value", type=click.STRING)
    def update_cli(key, value):
        """
        Will overwrite existing key values pairs in the file.
        """
        update(ctx["language"], key, value)
        write_json(ctx["file"], ctx["language"])

    cli()