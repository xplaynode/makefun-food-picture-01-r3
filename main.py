"""food-picture-01 entry (round 3): put the food picture in the output.

The picture is committed beside this file as ``entry.png``: a 1024x1024
JPEG (the gate accepts PNG or JPEG bytes under that name) of a single bowl
of tonkotsu ramen with a tall glossy noodle pull, a fan of charred chashu
and a molten ajitama egg dripping over the rim, chosen by a pairwise
tournament over 12 generated candidates (see tournament.md). It is the
round-3 improvement entry: the live leaderboard's top places are all this
exact shape -- one bowl, one dramatic noodle pull, molten egg, steam, dark
table -- so the incumbent static yolk-break shot was replaced with the
strongest pull composition from the tournament.

The program copies those exact bytes to the output path, so repeat runs
are byte-identical. The output path is, in order: the first command-line
argument when one is given (a file path, or a directory to write
``entry.png`` into), else ``$MAKEFUN_OUTPUT_DIR/entry.png`` when that
variable is set (the kit's local runs set it), else ``/output/entry.png``
(the grading sandbox). Standard library only, no network.
"""

import hashlib
import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def digest(path: str) -> str:
    """sha256 of a file, read in chunks so the whole image is never held
    in memory at once."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def resolve_output(argv: list) -> str:
    """Work out where the picture goes for this run."""
    if len(argv) > 1:
        target = argv[1]
        if os.path.isdir(target):
            return os.path.join(target, "entry.png")
        return target
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.png")


def main(argv: list) -> int:
    dest = resolve_output(argv)
    parent = os.path.dirname(os.path.abspath(dest))
    os.makedirs(parent, exist_ok=True)
    shutil.copyfile(SOURCE, dest)
    # The entry is graded on the exact bytes written, and the program runs
    # twice and must produce the same bytes both times: verify the copy
    # landed whole (the written file's sha256 matches the committed
    # picture) rather than trusting the copy call, so a truncated write
    # fails this run loudly instead of grading a broken image.
    if digest(dest) != digest(SOURCE):
        print("error: output does not match entry.png", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({os.path.getsize(dest)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
