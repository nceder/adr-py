"""
    adr-py main module



"""

import argparse
import os.path

import init_directory
import util
import update_adr

allowed_commands = (
    "init",
    "new",
    "accept",
    "supercede",
    "reject",
    "link",
    "related",
    "list",
)


def get_args():
    """args:
    -d location of ADR's
    -f location of .adr-config
    NOT IMPLEMENTED -c config file to use
    """
    parser = argparse.ArgumentParser(
        description="Manage Architecture Design Records - ADR's.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-d",
        dest="adr_dir",
        action="store",
        default="docs/adrs",
        help="path to directory of ADR files",
    )
    parser.add_argument(
        "-f",
        dest="adr_dir_file",
        action="store",
        default=".adr-dir",
        help="path of .adr-dir file",
    )
    parser.add_argument(
        "command",
        type=str,
        metavar="<command>",
        default=None,
        help="""init <directory to init> - inits (creates if necessary) new directory,
new <description of new ADR> - creates new ADR using description for title, 
accept <ADR number or prefix> - marks ADR as Accepted, 
reject <ADR number or prefix> - marks ADR as Rejected, 
supercede <old ADR number or prefix> <new ADR number or prefix> - marks old ADR 
             as superceded by new one, 
link  <ADR number or prefix>  <ADR number or prefix> - marks two ADR's as related, 
related  <ADR number or prefix> <description of new ADR> - creates a new ADR and 
             marks it as related to other one, 
list [full|status|filename [<ADR number or prefix>]> - prints listings of either 
             all ADR's or specified ADR to stdout in requested format. 
             No params = status format, all ADR's""",
    )
    parser.add_argument(
        "params",
        type=str,
        nargs="*",
        default="",
        help="description of the ADR or additional params",
    )
    args = parser.parse_args()
    if args.command not in allowed_commands:
        raise ValueError(f"{args.command} not in allowed list {allowed_commands}")
    return args


def main():
    args = get_args()
    adr_dir_file = args.adr_dir_file
    try:
        with open(args.adr_dir_file) as adr_dir_file:
            adr_dir_name = adr_dir_file.read().strip()
    except FileNotFoundError:
        adr_dir_name = args.adr_dir

    adr_dir = (
        os.path.expanduser(adr_dir_name)
        if adr_dir_name and adr_dir_name != args.adr_dir
        else os.path.expanduser(args.adr_dir)
    )
    command = args.command
    params = args.params
    if command == "init":
        if params:
            adr_dir_name = params[0]
        init_directory.init_adr_dir(adr_dir_name, args.adr_dir_file)

    elif command in ("new", "accept", "reject", "supercede", "link", "related"):
        update_adr.update_status(adr_dir_name, command, params[0], params[1:])
    elif command in ("list"):
        util.list_adrs(
            adr_dir_name,
            style=params[0] if params else "status",
            adr_num=params[1] if len(params) > 1 else None,
        )

if __name__ == "__main__":
    main()
