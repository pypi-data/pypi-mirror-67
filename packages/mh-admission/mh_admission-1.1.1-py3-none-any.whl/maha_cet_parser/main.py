"""Main entry point for pcd module"""

import sys
import logging

import maha_cet_parser.commands

logging.basicConfig(level=logging.INFO)


def maha_cet_parser_tools_cli():
    """CLI entry point for the app"""
    sys.exit(cli_from_args(sys.argv[1:]))


def cli_from_args(args):
    args = maha_cet_parser.commands.Command.parse_args(args)
    return args.func(args)


if __name__ == "__main__":
    maha_cet_parser_tools_cli()
