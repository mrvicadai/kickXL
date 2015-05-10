# -*- coding: utf-8 -*-
"""
cli for kickass-xl tool
"""

import argparse


def build_kickass_parser(parser):
    parser.add_argument("query",
                        help="The query given to kickassAPI")


def use_kickass(options):
    pass


def main():
    """
    entry point for the kickass xunlei tool
    """
    parser = argparse.ArgumentParser(description="kickass + XL utility")

    subparsers = parser.add_subparsers(title="subcommands",
                                       dest="subcommands")

    # ---------------------
    # list of sub_parsers |
    # ---------------------

    kickass_parser = subparsers.add_parser("kickass")

    # ----------------------
    # implement subparsers |
    # ----------------------

    build_kickass_parser(kickass_parser)

    options = parser.parse_args()

    if options.subcommand == "kickass":
        use_kickass(options)

if __name__ == '__main__':
    main()
