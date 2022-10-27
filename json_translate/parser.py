#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import argparse

from settings import (
    INDENTATION_DEFAULT,
    SLEEP_BETWEEN_API_CALLS,
)


def get_parser(prog_name):
    """
    Constructs and returns the argument parser for all commands.
    """

    if not os.environ.get("DEEPL_AUTH_KEY", False):
        # TODO: Set as argument with default from env vars
        raise Exception("Environment variables not loaded")

    parser = argparse.ArgumentParser(
        prog=prog_name,
        description="Translate json files using the DeepL API ",
        epilog="Report issues at https://github.com/Saigesp/json-deepl-translate/issues",
    )
    parser.add_argument(
        "file",
        help="Folder or file to look for translation source",
    )
    parser.add_argument(
        "-l",
        "--locale",
        default="en",
        help="Language target to translate",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="en.json",
        help="Output file name",
    )
    parser.add_argument(
        "-i",
        "--indent",
        type=int,
        default=INDENTATION_DEFAULT,
        help="Indentation spaces",
    )
    parser.add_argument(
        "-s",
        "--sleep",
        type=float,
        default=SLEEP_BETWEEN_API_CALLS,
        help="Sleep time between API calls",
    )
    parser.add_argument(
        "--skip",
        nargs="+",
        help="Keys to skip",
    )

    return parser
