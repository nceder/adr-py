import pathlib
import re


def parse_adr_directory(adr_directory):
    adr_path = ensure_path(adr_directory)
    adr_file_paths = [
        (int(x.name.split("-")[0]), x)
        for x in adr_path.glob("[09]*.md")
        if x.name.split("-")[0].isdigit()
    ]
    adr_file_paths.sort()
    if not adr_file_paths:
        adr_file_paths.append([0, None])
    return adr_file_paths


def write_adr(adr_path, adr_text):
    with open(adr_path, "w") as adr_file:
        adr_file.write(adr_text)


def get_next_adr_number(adr_directory):
    next_adr_number = parse_adr_directory(adr_directory)[-1][0] + 1
    return next_adr_number

def ensure_path(filepath):
    adr_path = pathlib.PosixPath(filepath)
    return adr_path

def find_adr(adr_path, adr):
    adr_dir_list = parse_adr_directory(adr_path)
    try:
        old_adr_num = int(adr)
        old_adr = [x[1] for x in adr_dir_list if x[0] == old_adr_num][
            0
        ]
    except ValueError:
        try:
            old_adr = [
                str(x[1])
                for x in adr_dir_list 
                if x[1].name.startswith(adr)
            ][0]
        except IndexError:
            raise ValueError(f"{adr} not found.")
    return old_adr


def load_adr(adr_file_name):
    adr_path = pathlib.PosixPath(adr_file_name)
    with open(adr_path) as adr_file:
        adr_text = adr_file.read()
    return adr_path, adr_text


def parse_adr(adr_text):
    results = re.search(
        "# (?P<adr_num>\d+).+ (?P<title_text>[\s\w]+)\n.+Date: (?P<date_str>\d+-\d+-\d+).+"
        "## Status\s+(?P<status>\w+)\s+## Context(?P<context>.+)## Decision(?P<decision>.+)"
        "## Consequences(?P<consequences>.+)",
        adr_text,
        re.DOTALL,
    )
    adr_data = {
        "adr_num": int(results.group("adr_num").strip()),
        "title_text": results.group("title_text").strip(),
        "date_str": results.group("date_str").strip(),
        "status": results.group("status").strip(),
        "context": results.group("context").strip(),
        "decision": results.group("decision").strip(),
        "consequences": results.group("consequences").strip(),
    }
    return adr_data


def list_adrs(adr_path, adr_num=None, style="status"):
    if adr_num is not None:
        target_adr = find_adr(adr_path, adr_num)
        adr_list = [target_adr]
        adr_name = target_adr.name

    else:
        adr_list = [x[1] for x in parse_adr_directory(adr_path)]
        adr_name = "all ADR's"

    if style == "full":
        print(f"# Full text of {adr_name} in {adr_path}\n")
    for x in adr_list:
        _, adr_text = load_adr(x)
        adr_data = parse_adr(adr_text)
        if style == "status":
            print(
                f"{x}  : {adr_data['title_text']}, {adr_data['status']} {adr_data['date_str']}"
            )
        if style == "filename":
            print(f"{x}")
        elif style == "full":
            print(f"----\n{x}\n\n{adr_text}")
