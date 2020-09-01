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
    "title_text": "Record architecture decisions",
    "filename_text": "record-architecture-decisions",
    "date_str": "2020-08-30",
    "status": "Accepted",
    "context": "We need to record the architectural decisions made on this project.",
    "decision": (
        "We will use Architecture Decision Records, as described by Michael Nygard in this article: "
        "http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions"
    ),
    "consequences": "See Michael Nygard's article, linked above.",
}
base_adr_data = {
    "adr_num": None,
    "title_text": "",
    "filename_text": "",
    "date_str": "",
    "status": "Proposed",
    "context": "The issue motivating this decision, and any context that influences or constrains the decision.",
    "decision": "The change that we're proposing or have agreed to implement.",
    "consequences": (
        "What becomes easier or more difficult to do and any risks introduced "
        "by the change that will need to be mitigated."
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
