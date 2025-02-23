from pprint import pprint

from flask import current_app as app


@app.cli.command("show-config")
def show_config():
    config = {}
    for k, v in app.config.items():
        config[k] = v

    pprint(config, indent=2)
