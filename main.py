"""make.fun news-image-20261122 entry.

Writes the entry image to /output/entry.png. The image ships in this
repository as entry.png, next to this file; the program copies it
byte for byte, so every run produces exactly the same bytes.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.exists(src):
        src = os.path.join(os.getcwd(), "entry.png")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    with open(dst, "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
