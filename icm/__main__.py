# -*- coding: utf-8 -*-
# -- This file is part of the Icestudio project
# -- (C) 2017 FPGAwars
# -- Author Jesús Arroyo
# -- Licence GPLv2

import click

from sys import exit as sys_exit

from icm.commands import cmd_init


@click.group()
@click.version_option()
def cli():
    pass


@cli.command()
def init():
    """Initialize a collection structure."""
    cmd_init.init()
