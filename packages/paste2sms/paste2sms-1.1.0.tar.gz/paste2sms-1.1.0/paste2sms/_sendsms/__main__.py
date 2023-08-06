# Copyright 2020 Louis Paternault
#
# This file is part of paste2sms.
#
# Paste2sms is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Paste2sms is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Paste2sms.  If not, see <https://www.gnu.org/licenses/>.

"""Main script for sendsms."""

import argparse
import logging
import time

from .. import P2SException, VERSION
from .. import sendsms

SLEEP = 5


def commandline_parser():
    """Build and return the command line parser."""
    parser = argparse.ArgumentParser(
        prog=__package__,
        description="Send the message qiven in command line as an SMS.",
        epilog=(
            "Only the message is given as command line arguments. The recipient phone number (and other information) is read from the paste2sms configuration file."
        ),
    )

    parser.add_argument(
        "--version", action="version", version="%(prog)s {}".format(VERSION)
    )

    parser.add_argument(
        "-f",
        "--file",
        type=argparse.FileType("r"),
        action="append",
        help="Content of those files are sent as SMS (one SMS per file).",
        default=[],
    )

    parser.add_argument(
        "message", help="Message to be sent by SMS.", nargs=argparse.REMAINDER,
    )

    return parser


def main():
    """Main function."""
    logging.basicConfig(level=logging.INFO)

    # Parse command line arguments
    options = commandline_parser().parse_args()
    if options.message:
        if options.message[0] == "--":
            del options.message[0]

    messages = []
    for file in options.file:
        messages.append(file.read())
    if options.message:
        messages.append(" ".join(options.message))

    first = True
    for content in messages:
        if first:
            first = False
        else:
            time.sleep(SLEEP)

        try:
            sendsms(content)
        except P2SException as error:
            logging.log(level=error.level, msg=str(error))


if __name__ == "__main__":
    main()
