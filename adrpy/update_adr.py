"""
    given either the ADR number or full filename, read and parse and exsitng file name
    and do one of the following:

      - approve - change status from "Proposed" to "Accepted", add approval datestamp
      - reject - change status to "Rejected", add rejection datestamp
      - supercede - change status to "Superceded", create link to ADR replacing it, add superceded timestamp
      - line - add link to ADR specified

"""

from . import util
from . import new_adr

explanations = {
    "link": ["RELATED to", "RELATED to"],
    "related": ["RELATED to", "RELATED to"],
    "supercede": ["SUPERCEDED by", "SUPERCEDES"],
}

updated_status = {
    "accept": "Accepted",
    "reject": "Rejected",
    "supercede": "Superceded",
}


def update_status(adr_path, command, old_adr, params):
    if command == "new":
        title_list = [old_adr] + params
        old_adr_path, old_adr_text = new_adr.create_adr(
            adr_path, title_list
        )
    else:
        old_adr = util.find_adr(adr_path, old_adr)

        old_adr_path, old_adr_text = util.load_adr(old_adr)
        old_adr_data = util.parse_adr(old_adr_text)
        old_title_list = old_adr_data["title_text"].split(" ")
        old_adr_data["status"] = (
            updated_status[command]
            if updated_status.get(command)
            else old_adr_data["status"]
        )
        if command in updated_status:
            old_adr_data["date_str"] = ""

        if command in ("related", "supercede", "link"):
            if command in ("link", "supercede"):
                adr = params[0]
                adr = util.find_adr(adr_path, adr)
                new_adr_path, new_adr_text = util.load_adr(adr)
                new_adr_data = util.parse_adr(new_adr_text)
                if command == "supercede":
                    new_adr_data["date_str"] = ""
                new_title_list = new_adr_data["title_text"].split(" ")
            else:
                new_adr_data = dict(new_adr.base_adr_data)
                new_title_list = params

            new_adr_data["context"] += f"\n\n{explanations[command][1]} {old_adr_path}"
            new_adr_path, new_adr_text = new_adr.create_adr(
                adr_path, new_title_list, base_adr_data=new_adr_data
            )
            util.write_adr(new_adr_path, new_adr_text)
            old_adr_data["context"] += f"\n\n{explanations[command][0]} {new_adr_path}"

        old_adr_path, old_adr_text = new_adr.create_adr(
            adr_path, old_title_list, base_adr_data=old_adr_data
        )
    util.write_adr(old_adr_path, old_adr_text)
