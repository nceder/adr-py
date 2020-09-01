"""
    Write a new ADR file, incrementing ADR number from highest in adr_dir,
    file name and title from title given on by user


"""

import datetime as dt
from . import util


adr_template = """# {adr_num}. {title_text}

Date: {date_str}

## Status

{status}

## Context

{context}

## Decision

{decision}

## Consequences

{consequences}

"""
first_adr_data = {
    "adr_num": 1,
    "title_text": "Architecture decisions folder initialized",
    "filename_text": "architecture-decision-folder-initialized",
    "date_str": "",
    "status": "Accepted",
    "context": "Placeholder first ADR",
    "decision": (
        "This is a place holder to initialize the folder for storing ADR's. You can replace this content "
        "and use for an ADR, and you can rename the file, as long as you preserve the structure/headings and "
        "begin the filename with '0001'." 
    ),
    "consequences": "For more on Architecture Decision Records, refer to Michael Nygard's article: "
        "http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions"
}
base_adr_data = {
    "adr_num": None,
    "title_text": "",
    "filename_text": "",
    "date_str": "",
    "status": "Proposed",
    "context": "Brief description of the problem, constraints, and other considerations (pro's/con's) for this ADR",
    "decision": "Brief descripton of the change to be made.",
    "consequences": (
        "How will this change improve the project going forward? "
        "What considerations, risks, or other issues will need to considered or mitigated?"
    ),
}


def create_adr(
    adr_path, title_list, base_adr_data=base_adr_data, adr_template=adr_template
):
    adr_data = dict(base_adr_data)
    adr_num = (
        int(adr_data["adr_num"])
        if adr_data["adr_num"]
        else util.get_next_adr_number(adr_path)
    )
    adr_filename = f"{adr_num:04}-{'-'.join(title_list).lower()}.md"
    title_text = " ".join(title_list)
    date_str = (
        adr_data["date_str"]
        if adr_data["date_str"]
        else dt.date.today().strftime("%Y-%m-%d")
    )
    adr_data["adr_num"] = adr_num
    adr_data["date_str"] = date_str
    adr_data["title_text"] = title_text
    adr_data["filename_text"] = adr_filename
    adr_path = util.ensure_path(adr_path).joinpath(adr_filename)
    return adr_path, adr_template.format(**adr_data)


def first_adr(adr_path):

    full_adr_path, adr_text = create_adr(
        adr_path,
        title_list=("Record", "architecture", "decisions"),
        base_adr_data=first_adr_data,
    )
    if int(full_adr_path.name.split("-")[0]) > 1:
        raise ValueError(f"Directory {adr_path} already initialized, no action taken.")
    return full_adr_path, adr_text
