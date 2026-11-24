"""Entrypoint: render the 24 November 2026 front page to /output/entry.png."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gen_image import build

OUT = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    build(OUT)
    size = os.path.getsize(OUT)
    print(f"wrote {OUT} ({size} bytes, 1024x1024)")


if __name__ == "__main__":
    main()
