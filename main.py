"""Writes the entry: one satirical sentence (216 characters) roasting lawmakers who regulate AI badly.

The sandbox runs it offline, once per grade; it only writes /output/entry.txt.
"""

import pathlib

LINE = (
    "They cannot convert a file to PDF, so they will regulate the conversion. "
    "Expect a 400-page bill, emailed as a screenshot, requiring every AI to "
    "print itself out and fax a copy to a committee that lost the attachment."
)


def main() -> None:
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
