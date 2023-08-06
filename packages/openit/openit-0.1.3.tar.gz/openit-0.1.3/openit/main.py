import shlex
import subprocess

import click

from pobject import P


@click.command()
@click.argument('arg')
def main(arg):

    config_dict = _get_config_dict()
    sites_dict = config_dict['sites']
    if arg in sites_dict:
        url = sites_dict[arg]
        command = f'google-chrome --new-window {url}'
        subprocess.call(shlex.split(command))
    else:
        print('No match')


def _get_config_dict():
    config_dict = P('openit/config.yaml').to_dict()
    return config_dict

